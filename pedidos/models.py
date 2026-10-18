from django.db import models
from django.conf import settings
from catalogo.models import Variante

class Pedido(models.Model):
    ESTADOS = {
        'pendiente': 'Pendiente',
        'pagado': 'Pagado',
        'enviado': 'Enviado',
    }

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='pedidos',
    )
    variantes = models.ManyToManyField(
            Variante,
            through='LineaPedido',
            related_name='pedidos',
        )
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return f'Pedido {self.id}'

class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='lineas')
    variante = models.ForeignKey(Variante, on_delete=models.PROTECT, related_name='lineas')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pedido', 'variante'], name='linea_unica_por_variante'
            ),
        ]

    def __str__(self):
        return f'{self.cantidad} x {self.variante}'

class Factura(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.PROTECT)
    numero = models.CharField('número', max_length=20, unique=True)
    emitida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numero