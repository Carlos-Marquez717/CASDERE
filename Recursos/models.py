from django.db import models

# Create your models here.
class Biblias(models.Model):
    Nombre=models.CharField(max_length=50)
    version_año=models.DateField(auto_now_add=True) 
    url=models.URLField(max_length=200)

    class Meta:
        verbose_name='Biblia'
        verbose_name_plural='Biblias'   

    def _str_(self):
        return self.Nombre 

class Discipulado(models.Model):
    Nombre=models.CharField(max_length=50)
    Fecha=models.DateField(auto_now_add=True) 
    Descarga=models.CharField(max_length=200)

    class Meta:
        verbose_name='Discipulado'
        verbose_name_plural='Discipulados'   

    def _str_(self):
        return self.Nombre

class Libro(models.Model):
    Nombre=models.CharField(max_length=50)
    autor=models.CharField(max_length=50) 
    descarga=models.CharField(max_length=200)

    class Meta:
        verbose_name='Libro'
        verbose_name_plural='Libros'   

    def _str_(self):
        return self.Nombre                  