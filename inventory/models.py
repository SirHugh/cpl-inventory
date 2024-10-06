from django.db import models

# Create your models here.

class Item(models.Model):
    SKU = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    marca  = models.CharField(max_length=100) 
    categoria = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name 
    
class Almacen(models.Model):
    codigo = models.CharField(max_length=25, unique=True)
    nombre = models.CharField(max_length=100)
    sucursal = models.CharField(max_length=100)
    esActivo = models.BooleanField(default=True)
    
    
class ControlInventario(models.Model):
    fechaInicio = models.DateField(auto_now=True, auto_now_add=False)
    fechaFin = models.DateField(null=True, blank=True)
    esActivo = models.BooleanField(default=True)
    cantArticulos= models.IntegerField(blank=True, null=True)
    cantContada = models.IntegerField(default=0)
    almacen = models.ForeignKey("inventory.Almacen", on_delete=models.CASCADE)

class DetalleControl(models.Model):
    control = models.ForeignKey("inventory.ControlInventario", on_delete=models.CASCADE)
    item = models.ForeignKey("inventory.Item", on_delete=models.CASCADE)
    cantContada = models.IntegerField(default=0)
    stockSap = models.IntegerField()
    diferencia = models.IntegerField()
    
class RecuentoDetalle(models.Model):
    detalleControl = models.ForeignKey("inventory.detalleControl", on_delete=models.CASCADE)
    fechaHora = models.DateField()
    stockSap = models.IntegerField()
    recuento = models.IntegerField()    
    
    
    
    

        

    