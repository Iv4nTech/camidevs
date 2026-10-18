from django.contrib import admin, messages

from .models import Categoria, Consulta, Etiqueta, Producto, Variante

admin.site.site_header = 'Administración de CamiDevs'
admin.site.site_title = 'CamiDevs'
admin.site.index_title = 'Panel de gestión'

admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'activo', 'creado']
    list_filter = ['activo', 'categoria']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio']
    readonly_fields = ['creado']
    actions = ['ocultar']
    filter_horizontal = ['etiquetas']

    @admin.action(description='Ocultar los productos seleccionados')
    def ocultar(self, request, queryset):
        ocultados = queryset.update(activo=False)
        self.message_user(request, f'Productos ocultados: {ocultados}.', messages.SUCCESS)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'asunto', 'leido', 'creado']
    list_filter = ['leido', 'asunto']

admin.site.register(Etiqueta)

@admin.register(Variante)
class VarianteAdmin(admin.ModelAdmin):
    list_display = ['producto', 'talla', 'color', 'stock']
    list_filter = ['talla', 'producto__categoria']