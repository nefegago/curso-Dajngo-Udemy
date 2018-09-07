from django.shortcuts import render
from .models import service

# Create your views here.

def services(request):
	context=service.objects.all()
	return render(request,'services.html',{'context':context})