#- * -coding: utf-8 - * -
from django.db import models
from .models import *
from datetime import datetime
from insumo.models import Insumo


class Entrada(models.Model):
    id_entrada = models.AutoField('ID', primary_key=True, unique=True)
    requisicion=models.IntegerField('No Requiscion')
    fecha_entrada=models.DateField('Fecha de Entrada')


    def __str__(self):
        return '%s, %s' % (self.requisicion, self.id_entrada)

    class Meta():
        db_table = 'entrada'
        verbose_name='Entrada'
        verbose_name_plural = 'Entradas'

class DetalleEntrada(models.Model):
    entrada = models.ForeignKey(
        Entrada, verbose_name='Entrada', on_delete=models.CASCADE)
    #insumo = models.ForeignKey(
     #   Insumo, verbose_name='Insumo',on_delete=models.CASCADE)
    insumo= models.ForeignKey(
        Insumo, verbose_name='Nombre Insumo', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(
        'Cantidad', help_text='solo incluir numeros')


    def __str__(self):
       return "%s : %s" % (self.insumo, self.cantidad)


    def save(self, force_insert=False, force_update=False, using=None):
        from django.db import transaction
        if not self.pk:
           isnew = True
        else:
           isnew = False

        with transaction.atomic():
            if isnew:
                self.insumo.existencia = self.insumo.existencia + self.cantidad
          #      subtotal=self.insumo.cantidad * self.insumo.precio
            super(DetalleEntrada, self).save(force_insert, force_update, using)
        self.insumo.save()


    #def __str__(self):
    #    return "{} {} {}".format(self.id_insumo, self.cantidad)

   # def save(self, forve_insert=False, force_update=False, usgin=None, update_fields=None):
    #self.cantidad = self.insumo.cantidad + self.DetalleEntrada.cantidad
    #super ().save(force_insert, force_update, using, update_fields)

    #def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # Suponiendo que "valor" es el valor del producto
    #self.total = self.idproducto1.valor + self.idproducto1.valor
        # para python 2.x la función super se escribe super(MiModelo, self)
    #super().save(force_insert, force_update, using, update_fields)

class Meta:
      db_table = 'entradadetalle'
      verbose_name='Entrada detalle'
      verbose_name_plural ='Entradas detalles'

    