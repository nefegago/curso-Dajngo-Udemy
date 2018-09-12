from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Website)
class WebsiteConfig(admin.ModelAdmin):
	readonly_fields = ['created', 'updated']
