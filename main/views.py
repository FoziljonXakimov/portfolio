import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Certificate, Message


def index(request):
    """Portfolio bosh sahifasi"""
    certificates = Certificate.objects.all()
    return render(request, 'index.html', {'certificates': certificates})


@csrf_exempt
@require_http_methods(["POST"])
def send_message(request):
    """Contact formadan xabar qabul qilish"""
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return JsonResponse({'success': False, 'error': 'Barcha maydonlarni to\'ldiring!'}, status=400)

        Message.objects.create(name=name, email=email, message=message)
        return JsonResponse({'success': True, 'message': 'Xabaringiz yuborildi!'})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def get_certificates(request):
    """Sertifikatlarni JSON formatda qaytarish"""
    certs = Certificate.objects.all().values('id', 'title', 'issuer', 'year', 'image')
    certs_list = []
    for cert in certs:
        if cert['image']:
            cert['image'] = request.build_absolute_uri('/media/' + cert['image'])
        certs_list.append(cert)
    return JsonResponse({'certificates': certs_list})
