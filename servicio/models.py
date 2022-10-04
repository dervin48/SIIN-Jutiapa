from django.db import models

class Servicio(models.Model):
    id_servicio = models.AutoField('ID', primary_key=True, unique=True)
    nombre = models.CharField('nombre de Servicio', max_length=50)
    descripcion = models.CharField('Descripción', max_length=50)
   
    def __str__(self):
        return "%s, %s" % (self.descripcion, self.nombre)

    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellido = self.descripcion.upper()

        super(Servicio, self).save()

    class Meta():
        db_table = 'servicio'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    #    unique_toguether = ['id_solicitante']


