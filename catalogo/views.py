from django.shortcuts import render, get_object_or_404

from .models import Categoria, Producto


def inicio(request):
    contexto = {
        'categorias': Categoria.objects.all(),
        'productos': Producto.objects.filter(activo=True),
    }
    return render(request, 'catalogo/inicio.html', contexto)


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id, activo=True)
    return render(request, 'catalogo/detalle_producto.html', {'producto': producto})
