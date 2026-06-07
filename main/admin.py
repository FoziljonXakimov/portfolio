from django.contrib import admin
from .models import Certificate, Message


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'year', 'created_at')
    search_fields = ('title', 'issuer')
    list_filter = ('year',)
    fields = ('title', 'issuer', 'year', 'image')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['image'].required = False
        form.base_fields['image'].help_text = "Rasm qo'shmasangiz ham bo'ladi — ixtiyoriy"
        return form


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('name', 'email')
    readonly_fields = ('name', 'email', 'message', 'sent_at')

    def has_add_permission(self, request):
        return False
