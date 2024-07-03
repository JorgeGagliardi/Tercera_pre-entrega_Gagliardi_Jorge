from django.db import models

# Create your models here.

class Plantas(models.Model):
    nombre = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    
    def __str__ (self):
        return f"{self.nombre}, {self.image}"
    
    class Meta:
        verbose_name = 'Plantas'
        verbose_name_plural = 'Plantas'
        
class Jardines(models.Model):
    nombre = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__ (self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = 'Jardines'
        verbose_name_plural = 'Jardines'

class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    paso_numero = models.IntegerField()
    paso_titulo = models.CharField(max_length=50)
    paso_nombre = models.CharField(max_length=50)
    paso_descripcion = models.CharField(max_length=1000)
    paso_image = models.CharField(max_length=50)
    
    def __str__ (self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = 'Cultivos'
        verbose_name_plural = 'Cultivos'
        
class Contactos(models.Model):
    apellido = models.CharField(max_length=50)
    ciudad   = models.CharField(max_length=50)
    pais     = models.CharField(max_length=50)
    correo   = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    mensaje  = models.CharField(max_length=240)

    def __str__ (self):
        return f"{self.apellido}"
    
    class Meta:
        verbose_name = 'Contactos'
        verbose_name_plural = 'Contactos'
    
