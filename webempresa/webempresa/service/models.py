from django.db import models

# Create your models here.

class service(models.Model):
	
	title = models.CharField(max_length=200, verbose_name="Titulo")
	subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
	content = models.TextField(verbose_name="Contenido")
	image = models.ImageField(upload_to='services', verbose_name="Imagen")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Actualizacion")

	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name= 'servicio'
