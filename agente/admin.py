from django.contrib import admin

from agente.models import Agente

class AgenteAdmin(admin.ModelAdmin):
    list_display=( 'nombre', 'perfil', 'is_active')
    
    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Agente'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Agente'


admin.site.register(Agente, AgenteAdmin)