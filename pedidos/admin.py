from django.contrib import admin
from .models import Factura, Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'estado', 'creado']
    list_filter = ['estado']


admin.site.register(Factura)