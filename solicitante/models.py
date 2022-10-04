from django.db import models
from comun.models import Persona

class Solicitante(Persona):
    id_solicitante = models.AutoField('ID', primary_key=True, unique=True)
    fecha_iniciolabores = models.DateField('fecha inicio labores')
   # nombre = models.CharField('nombres', max_length=50)
    #apellido = models.CharField('apellidos', max_length=50)
    #cargo = models.CharField('cargo', max_length=30)
  


    def __str__(self):
        return '%s, %s' %(self.apellido, self.nombre)

    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()

        super(Solicitante, self).save()


    class Meta():
        db_table = 'solicitante'
        verbose_name = 'Solicitante'
        verbose_name_plural = 'Solicitantes'
    #    unique_toguether = ['id_solicitante']


