from django.contrib import admin

from empresa.models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'is_active')
    list_filter=('is_active',)
    search_fields=('nombre',)
    ordering=('nombre',)

    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Empresas'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Empresas'

admin.site.register(Empresa, EmpresaAdmin)
