from django.contrib import admin
from .models import *


class DetalleSolicitudInline(admin.TabularInline):
    model = DetalleSolicitud
    extra = 0
    #autocomplete_fields = ['insumo']

class SolicitudAdmin(admin.ModelAdmin):
    inlines = [DetalleSolicitudInline]
    search_fields =['insumo']
    list_filter = ['solicitante', 'requisicion']
    list_display = ['solicitante', 'requisicion']
 #   readonly_field = ['solicitante']


admin.site.register(Solicitud, SolicitudAdmin)

