from django.db import models

# Create your models here.

class Portfolio(models.Model):
    """
    Description: Model Description
    """
    
    titulo = models.CharField(max_length=250, verbose_name='Titulo')
    descripcion = models.TextField(verbose_name='Descripcion')
    imagen = models.ImageField(upload_to="portafolio")
    create = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')

    class Meta:
        verbose_name='Portafolio'

    def __str__(self):
    	return self.titulo