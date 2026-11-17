from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.views.generic import ListView

from pedidos.models import LineaPedido

from .forms import RegistroForm


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


class PerfilView(LoginRequiredMixin, ListView):
    template_name = 'cuentas/perfil.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        return (
            self.request.user.pedidos
            .select_related('factura')
            .prefetch_related(
                Prefetch('lineas', queryset=LineaPedido.objects.select_related('variante__producto'))
            )
        )
