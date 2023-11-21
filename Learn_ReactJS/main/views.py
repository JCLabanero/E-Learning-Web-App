from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Learn1
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

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
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            # login(request,user)
            return redirect("main:login")
        else:
            for fields in form:
                for error in fields.errors:
                    messages.error(request,f"{fields.label}: {error}")
            return render(
            request,
            "main/register.html",
            context={"form": form}
            )

    form = UserCreationForm
    return render(request,
                "main/register.html",
                context={"form":form})