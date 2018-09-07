from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
	return render(request, 'index.html')

def about(request):
	return render(request,'about.html')

def store(request):
	return render(request,'store.html')

def contact(request):
	return render(request,'contact.html')

def sample(request):
	return render(request,'sample.html')

