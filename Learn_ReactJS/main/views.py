from django.shortcuts import render
from django.http import HttpResponse
from .models import Learn1
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def homepage(request):
    # return HttpResponse("Hello, World")
    return render(request=request,
                  template_name="main/home.html",
                  context={"Learn1":Learn1.objects.all})

def login(request):
    return render(request=request,
                  template_name="main/login.html")

def register(request):
    form = UserCreationForm
    return render(request,
                  "main/register.html",
                  context={"form":form})