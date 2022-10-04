from django.db import models
from insumo.models import Insumo
from solicitante.models import Solicitante
from servicio.models import Servicio


class Solicitud(models.Model):
    id_solicitud= models.AutoField('ID', primary_key=True, unique=True)
    requisicion=models.IntegerField('No Requiscion')
    fecha_solicitud = models.DateField('Fecha Solicitud')
    solicitante = models.ForeignKey(
        Solicitante, verbose_name='Solicitante', on_delete=models.CASCADE)
    servicio = models.ForeignKey(
        Servicio, verbose_name='Servicio', on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.solicitante, self.servicio)

 
  #  def save (self, **kwargs):
   #     monto=0
    #    for d in self.detallesolicitud_set.all():
     #       monto += d.sub_total
      #  self.total = monto
#        super(Solicitud, self).save()

    class Meta():
        db_table = 'solicitud'
        verbose_name='Solicitud'
        verbose_name_plural ='Solicitudes'



class DetalleSolicitud(models.Model):
    solicitud = models.ForeignKey(
        Solicitud, verbose_name='Solicitud', on_delete=models.CASCADE)
    insumo= models.ForeignKey(
        Insumo, verbose_name='Nombre Insumo', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(
        'Cantidad', help_text='solo incluir numeros')
   # subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, null=True)

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
                self.insumo.existencia = self.insumo.existencia - self.cantidad
           #     subtotal=self.cantidad * self.insumo.precio
            super(DetalleSolicitud, self).save(force_insert, force_update, using)
        self.insumo.save()


   # def __str__(self):
    #        return "%s" % (self.comanda)
    
    #def save(self, **kwargs):
     #   self.sub_total = self.menu.precio * self.cantidad
        
      #  super(DetalleComanda, self).save()

       # self.total = self.sub_total
        #super(Comanda,self).all(*args, **kwargs)


        class Meta:
            db_table = 'solicituddetalle'
            verbose_name = 'Solicitud Detalle'
            verbose_name_plural = 'Solcitudes Detalles'




# Create your models here.
