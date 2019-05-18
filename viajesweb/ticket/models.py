from django.db import models
from package.models import Internacionale

# Create your models here.

class Pasajero(models.Model):
	id_pasajero = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=200)
	documento = models.IntegerField()
	asientos = models.SmallIntegerField()
	fecha = models.DateField()

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name='Pasajero'
		verbose_name_plural = 'Pasajeros'
		ordering =['-id_pasajero']

class Pasaje(models.Model):
	id_pasaje = models.AutoField(primary_key=True)
	pasajero = models.ForeignKey(Pasajero,on_delete=models.CASCADE)
	lugar = models.ForeignKey(Internacionale,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.pasajero.nombre

	class Meta:
		verbose_name = 'Boleto'
		verbose_name_plural = 'Boletos'
		ordering = ['-id_pasaje']

