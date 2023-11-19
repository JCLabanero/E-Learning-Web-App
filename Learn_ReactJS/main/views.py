from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Learn1
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

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
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request,user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request,
                  "main/register.html",
                  context={"form":form})