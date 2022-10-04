from django.contrib import admin
from .models import *


class SolicitanteAdmin(admin.ModelAdmin):

    search_fields = ['nombre','apellido']
    list_filter = ['fecha_iniciolabores']
    list_display = ['id_solicitante','nombre', 'apellido', 'fecha_iniciolabores']

admin.site.register(Solicitante, SolicitanteAdmin)

