from .models import Website

def website(request):
	website = Website.objects.all().order_by("title")
	return {"website":website}