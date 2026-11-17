from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'catalogo'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('producto/<int:pk>/', views.DetalleProductoView.as_view(), name='detalle_producto'),
    path('contacto/', views.ContactoView.as_view(), name='contacto'),
    path('consultas/', views.ConsultasPendientesView.as_view(), name='consultas_pendientes'),
    path('buscar/', views.BuscarView.as_view(), name='buscar'),
    path('aviso-legal/', TemplateView.as_view(template_name='catalogo/aviso_legal.html'), name='aviso_legal'),
    path('privacidad/', TemplateView.as_view(template_name='catalogo/privacidad.html'), name='privacidad'),

]
