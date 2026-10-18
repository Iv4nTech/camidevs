from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('contacto/', views.contacto, name='contacto'),
    path('consultas/', views.consultas_pendientes, name='consultas_pendientes'),
]
