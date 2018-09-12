from django.urls import path
from .views import *

urlpatterns =[
	path("<int:pages_id>/<slug:title>/",pages, name="pages")
] 