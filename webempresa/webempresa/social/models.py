from django.db import models

# Create your models here.

class Social(models.Model):
	key = models.SlugField(max_length=200, unique=True, verbose_name='Clave',)
	name = models.CharField(max_length=200, verbose_name='Red_social',)
	url = models.URLField(verbose_name="Enlace", max_length=200, blank=True, null=True)
	ico = models.CharField(verbose_name='Ico', max_length=200, default="fa-social-home")
	order = models.SmallIntegerField(verbose_name='Orden', default=0)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Actualizacion")

	def __str__(self):
		return self.key
		
	class Meta:
		verbose_name= 'Redes_sociales'
		ordering = ['order']