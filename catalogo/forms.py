from django import forms
from django.core.exceptions import ValidationError

from .models import Consulta


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nombre', 'email', 'asunto', 'numero_pedido', 'mensaje']

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        if 'http' in mensaje.lower():
            raise ValidationError('No se permiten enlaces en el mensaje.', code='enlace')
        return mensaje

    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get('asunto')
        numero_pedido = cleaned_data.get('numero_pedido')

        if asunto == 'pedido' and not numero_pedido:
            self.add_error('numero_pedido', 'Indica el número de pedido.')
        return cleaned_data
