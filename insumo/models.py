from django.db import models

class Insumo(models.Model):
    id_insumo = models.AutoField('ID Insumo', primary_key=True, unique=True)
    nombre_insumo= models.CharField('Nombre Insumo', max_length=50)
    unidad= models.CharField('Unidad de Medida', max_length=50)
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    existencia = models.IntegerField('Existencia',default=0, editable=False)


    def __str__(self):
        return "%s, %s" % (self.id_insumo, self.nombre_insumo)

    class Meta():
        db_table = 'insumo'
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos '

