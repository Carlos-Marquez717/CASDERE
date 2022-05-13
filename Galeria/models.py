from django.db import models

# Create your models here.
class Galeria(models.Model):
    Nombre=models.CharField(max_length=50)
    fecha=models.DateField(auto_now_add=True)
    album=models.CharField(max_length=50) 
    imagen=models.ImageField( )

    class Meta:
        verbose_name='nombre'
        verbose_name_plural='nombres'   

    def _str_(self):
        return self.Nombre 