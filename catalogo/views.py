from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import ContactoForm
from .models import Categoria, Consulta, Producto


class InicioView(ListView):
    queryset = Producto.objects.filter(activo=True)
    context_object_name = 'productos'
    template_name = 'catalogo/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class DetalleProductoView(DetailView):
    queryset = Producto.objects.filter(activo=True)
    template_name = 'catalogo/detalle_producto.html'


class ContactoView(CreateView):
    form_class = ContactoForm
    template_name = 'catalogo/contacto.html'
    success_url = reverse_lazy('catalogo:contacto')

    def form_valid(self, form):
        response = super().form_valid(form)
        datos = form.cleaned_data
        send_mail(
            f'Contacto web: {datos["asunto"]}',
            f'De: {datos["nombre"]} ({datos["email"]})\n'
            f'Pedido: {datos["numero_pedido"]}\n\n'
            f'{datos["mensaje"]}',
            'web@camidevs.com',
            ['hola@camidevs.com'],
        )
        messages.success(self.request, 'Mensaje enviado. Te responderemos pronto.')
        return response


class ConsultasPendientesView(PermissionRequiredMixin, ListView):
    permission_required = 'catalogo.view_consulta'
    queryset = Consulta.objects.filter(leido=False)
    context_object_name = 'consultas'
    template_name = 'catalogo/consultas_pendientes.html'


class BuscarView(ListView):
    template_name = 'catalogo/buscar.html'
    context_object_name = 'productos'
    paginate_by = 4

    def get_queryset(self):
        productos = Producto.objects.filter(activo=True)
        q = self.request.GET.get('q', '')
        color = self.request.GET.get('color', '')

        if q:
            productos = productos.filter(nombre__icontains=q)
        if color:
            productos = productos.filter(variantes__color__icontains=color).distinct()

        return productos.select_related('categoria')
