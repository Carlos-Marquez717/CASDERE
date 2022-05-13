
from django.db import models

# Create your models here.
class servicio(models.Model):
    Titulo=models.CharField(max_length=50)
    url=models.URLField(max_length=200) 
    created=models.DateField(auto_now_add=True) 
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'   

    def _str_(self):
        return self.Titulo
