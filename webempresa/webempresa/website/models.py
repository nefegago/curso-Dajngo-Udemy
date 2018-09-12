from django.db import models
from ckeditor.fields import RichTextField
#from tinymce import HTMLField

# Create your models here.
class Website(models.Model):
    """
    Description: Este modelo administra las'paginas de footer personalizadas
    """
    title = models.CharField(verbose_name='Titulo', max_length=200)
    content = RichTextField(verbose_name='Contenido')
    #content = HTMLField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Actualizacion")

    def __str__(self):
    	return self.title