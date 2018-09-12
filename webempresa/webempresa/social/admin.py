from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Social)
class Social_register(admin.ModelAdmin):
	pass