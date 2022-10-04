from django.contrib import admin
from .models import *

class ServicioAdmin(admin.ModelAdmin):

    search_fields = ['nombre','descripcion']
    list_filter = ['nombre']
    list_display = ['id_servicio','nombre', 'descripcion']

admin.site.register(Servicio, ServicioAdmin)


