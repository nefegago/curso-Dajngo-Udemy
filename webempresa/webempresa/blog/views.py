from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.

def blog(request):
	context = Publication.objects.all()
	return render(request,'blog.html',{'context':context})

def category_filter(request, category_id):
	context = get_object_or_404(Category,id=category_id)
	return render (request,'category.html',{'context':context} )