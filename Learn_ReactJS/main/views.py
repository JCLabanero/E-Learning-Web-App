from django.shortcuts import render
from django.http import HttpResponse
from .models import Learn1

# Create your views here.

def homepage(request):
    # return HttpResponse("Hello, World")
    return render(request=request,
                  template_name="main/home.html",
                  context={"Learn1":Learn1.objects.all})