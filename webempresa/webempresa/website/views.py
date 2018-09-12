from django.shortcuts import render, get_object_or_404
from .models import Website

# Create your views here.

def pages(request, pages_id, title):
	page = get_object_or_404(Website, pk=pages_id)
	return render(request,'sample.html', {'page':page})
