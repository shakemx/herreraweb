from django.contrib import admin

from modalidad.models import Modalidad

class ModalidadAdmin(admin.ModelAdmin):
    list_display=('seguro', 'nombre', 'is_active')
    list_filter=('is_active', 'seguro')
    search_fields=('nombre',)
    ordering=('seguro',)
    
    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Modalidad'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Modalidad'


admin.site.register(Modalidad, ModalidadAdmin)

