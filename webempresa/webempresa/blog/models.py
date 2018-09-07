from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Actualizacion")
	def __str__(self):
		return self.name

	class Meta():
		verbose_name='Categoria'
		verbose_name_plural='Categorias'



class Publication(models.Model):
	title = models.CharField(max_length=200, verbose_name='Titulo')
	category = models.ManyToManyField(Category,verbose_name="Categorias", related_name="get_category")
	image = models.ImageField(upload_to='blog', blank=True, null=True, verbose_name="Imagen")
	content = models.TextField(verbose_name="Contenido")
	autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor", related_name="get_users")
	published = models.DateTimeField(default=timezone.now, verbose_name= "Fecha Publicacion")
	created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha Creacion")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Actualizacion")

	def __str__(self):
		return self.title
	
	class Meta():
		verbose_name='publicacion'
		verbose_name_plural= 'publicaciones'




