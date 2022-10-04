from django.contrib import admin
from .models import *

class DetalleEntradaInline(admin.TabularInline):
    model = DetalleEntrada
    extra = 0
    #raw_id_fields = ['']
   # autocomplete_fields = ['insumo']

class EntradaAdmin(admin.ModelAdmin):
    inlines = [DetalleEntradaInline]
    search_fields = ['fecha_entrada']
    list_filter = ['fecha_entrada','requisicion',]
    list_display = ['fecha_entrada', 'requisicion']
    readonly_field = ['fecha_entrada']

admin.site.register(Entrada, EntradaAdmin)

