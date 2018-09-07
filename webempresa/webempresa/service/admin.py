from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(service)
class modeloservice(admin.ModelAdmin):
	readonly_fields = ['created', 'updated']