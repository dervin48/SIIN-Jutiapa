from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField('nombres', max_length=50)
    apellido = models.CharField('apellidos', max_length=50)
    cargo = models.CharField('cargo', max_length=30)
  

    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)

    class Meta():
        abstract = True 

