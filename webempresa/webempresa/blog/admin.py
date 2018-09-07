from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class ModelCategory (admin.ModelAdmin):
	readonly_fields = ['created', 'updated']
	verbose_name='Categoria'



@admin.register(Publication)	
class ModelPublication (admin.ModelAdmin):
	list_display = ["pk","title","content","autor",]
	list_display_links=["pk","title"]
	list_filter=["title",]
	search_fields = ['title']
	readonly_fields = ['created', 'updated',]
	verbose_name='Publicacion'
