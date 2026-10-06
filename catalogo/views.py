from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Categoria, Producto
from .forms import ContactoForm

from django.core.mail import send_mail

def inicio(request):
    contexto = {
        'categorias': Categoria.objects.all(),
        'productos': Producto.objects.filter(activo=True),
    }
    return render(request, 'catalogo/inicio.html', contexto)


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id, activo=True)
    return render(request, 'catalogo/detalle_producto.html', {'producto': producto})

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            datos = form.cleaned_data
            send_mail(
                f'Contacto web: {datos["asunto"]}',
                f'De: {datos["nombre"]} ({datos["email"]})\n'
                f'Pedido: {datos["numero_pedido"]}\n\n'
                f'{datos["mensaje"]}',
                'web@camidevs.com',
                ['hola@camidevs.com'],
            )
            messages.success(request, 'Mensaje enviado. Te responderemos pronto.')
            return redirect('catalogo:contacto')
    else:
        form = ContactoForm()

    return render(request, 'catalogo/contacto.html', {'form': form})