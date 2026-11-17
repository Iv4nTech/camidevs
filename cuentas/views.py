from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Prefetch
from django.shortcuts import render, redirect

from pedidos.models import LineaPedido

from .forms import RegistroForm
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, f'¡Bienvenido, {usuario.username}!')
            return redirect('catalogo:inicio')
    else:
        form = RegistroForm()

    return render(request, 'cuentas/registro.html', {'form': form})

@login_required
def perfil(request):
    pedidos = (
        request.user.pedidos
        .select_related('factura')
        .prefetch_related(
            Prefetch('lineas', queryset=LineaPedido.objects.select_related('variante__producto'))
        )
    )
    return render(request, 'cuentas/perfil.html', {'pedidos': pedidos})
