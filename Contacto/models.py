from django.db import models

# Create your models here.
class Contacto(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    telefono=models.IntegerField(max_length=12)
    Email=models.EmailField(max_length=50) 
    Asunto= models.CharField(max_length=50)
    Mensaje= models.CharField(max_length=200)

    class Meta:
        verbose_name='nombre'
        verbose_name_plural='nombres'   

    def _str_(self):
        return self.Nombre

    