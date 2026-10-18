from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, verbose_name='categoría', related_name='productos'
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField('descripción', blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    etiquetas = models.ManyToManyField(Etiqueta, related_name='productos', blank=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.nombre

class Variante(models.Model):
    TALLAS = {
        'S': 'S',
        'M': 'M',
        'L': 'L',
        'XL': 'XL',
    }

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='variantes',
    )
    talla = models.CharField(max_length=2, choices=TALLAS)
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.producto} ({self.talla}, {self.color})'


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
