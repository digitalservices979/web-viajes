from django.db import models
from django.conf import settings
import os
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver


def custom_upload_to(instance,filename):
    if Internacionale.objects.get(pk=instance.pk) is not None:
        old_instance = Internacionale.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return 'projects/' + filename
    else:
        return 'projects/'
    

# Create your models here.
class Nacionale(models.Model):
    id_nacional = models.AutoField(primary_key=True)
    lugar = models.CharField(max_length=50)  # Field name made lowercase.
    descripcion = models.TextField()  # Field name made lowercase.
    precio = models.DecimalField(max_digits=5,decimal_places=2)  # Field name made lowercase.
    imagen = models.ImageField(upload_to='projects')  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Fecha de creación")

    def __str__(self):
        return self.lugar

    class Meta:
        verbose_name="Nacional"
        verbose_name_plural="Nacionales"
        ordering = ['-created']

    

class Internacionale(models.Model):
    id_internacional = models.AutoField(primary_key=True)
    lugar = models.CharField(max_length=50)  # Field name made lowercase.
    descripcion = models.TextField()  # Field name made lowercase.
    precio = models.DecimalField(max_digits=5,decimal_places=2)  # Field name made lowercase.
    imagen = models.ImageField(upload_to='projects')
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Fecha de creación")

    def __str__(self):
        return self.lugar

    class Meta:  	
        verbose_name="Internacional"
        verbose_name_plural="Internacionales"
        ordering = ['-created']