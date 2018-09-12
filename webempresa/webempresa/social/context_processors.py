from .models import Social

def redes(request):
	social = Social.objects.all().order_by("order")
	return {"social":social}