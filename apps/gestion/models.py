from django.db import models
import datetime

# Create your models here.
class Cliente(models.Model):
	nombre					= models.CharField(max_length=100)
	fecha_nacimiento		= models.DateField(default=datetime.date.today,blank=True,null=True)
	telefono_numero 		= models.CharField(max_length=10, null=True)
	direccion				= models.CharField(max_length=100, null=True)
	otro_contacto			= models.CharField(max_length=150, null=True)

	def __unicode__(self):
		return u'%s' % self.nombre	


class Vehiculo(models.Model):
	
	tipo_vehiculo	= models.CharField(max_length=20)
	modelo_marca	= models.CharField(max_length=100)
	patente 		= models.CharField(max_length=12,unique=True)
	observaciones	= models.CharField(max_length=100,null=True)

	def __unicode__(self):
		return u'%s - %s' % (self.modelo_marca,self.patente)

class Trabajo(models.Model):
	vehiculo 			= models.ForeignKey(Vehiculo,related_name='trabajos_realizados')
	fecha_ingreso 		= models.DateField(null=True)
	fecha_entrega		= models.DateField(null=True)
	km_ingreso			= models.IntegerField(null=True)
	descripcion			= models.CharField(max_length=250,null=True)
	estado 				= models.IntegerField()
	precio 				= models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __unicode__(self):
		return u'%s' % self.descripcion

class ClienteVehiculo(models.Model):
	vehiculo 			= models.ForeignKey(Vehiculo,related_name='pertenece_a')
	cliente 			= models.ForeignKey(Cliente,related_name='tiene')
	fecha 				= models.DateField()
	fecha_hasta 		= models.DateField(null=True)
