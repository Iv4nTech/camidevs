from django.urls import path

from . import views

app_name = 'cuentas'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
    
]