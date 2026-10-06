from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, verbose_name='categoría'
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField('descripción', blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.nombre


class Consulta(models.Model):
    ASUNTOS = {
        'pedido': 'Un pedido',
        'producto': 'Un producto',
        'otro': 'Otra consulta',
    }

    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=20, choices=ASUNTOS, default='otro')
    numero_pedido = models.CharField(
        'número de pedido',
        max_length=20,
        blank=True,
        help_text='Lo encontrarás en el email de confirmación.',
    )
    mensaje = models.TextField()
    leido = models.BooleanField('leído', default=False)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return f'{self.nombre} ({self.email})'
