from django.contrib import admin
from .models import *

class InsumoAdmin(admin.ModelAdmin):

    search_fields = ['nombre_insumo','id_insumo']
    list_filter = ['precio']
    list_display = ['id_insumo','nombre_insumo','existencia','unidad', 'precio']

admin.site.register(Insumo, InsumoAdmin)


