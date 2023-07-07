from django.contrib import admin

from seguro.models import Seguro, Producto, TipoSeguro
from empresa.models import Empresa

class SeguroAdmin(admin.ModelAdmin):
    list_display=('empresa', 'nombre', 'is_active')
    list_filter=('is_active', 'empresa')
    search_fields=('nombre',)
    ordering=('nombre',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'empresa':
            kwargs["queryset"] = Empresa.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
        

    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Seguro'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Seguro'

class ProductoAdmin(admin.ModelAdmin):
    list_display=('seguro', 'producto', 'is_active')
    list_filter=('is_active', 'seguro')
    search_fields=('producto',)
    ordering=('seguro', 'producto')

    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Seguro'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Seguro'


class TipoSeguroAdmin(admin.ModelAdmin):
    list_display=('producto', 'tipo', 'is_active')
    list_filter=('is_active', 'tipo', 'producto',)
    search_fields=('tipo',)
    ordering=('tipo',)

    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Seguro'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Seguro'




admin.site.register(Seguro, SeguroAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoSeguro, TipoSeguroAdmin)