from django.contrib import admin
from .models import * 

# Register your models here.

#admin.site.register(Portfolio)
#or
@admin.register(Portfolio)
class Portfolioregister(admin.ModelAdmin):
	readonly_fields= ["create", "update"]