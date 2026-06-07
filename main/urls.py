from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-message/', views.send_message, name='send_message'),
    path('api/certificates/', views.get_certificates, name='certificates'),
]
