from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    contexto = {
        'titulo': 'CamiDevs',
        'categorias': ['Camisetas', 'Sudaderas', 'Accesorios'],
    }
    return render(request, 'catalogo/inicio.html', contexto)


def detalle_producto(request, id):
    return HttpResponse(f"Producto con ID: {id}")
