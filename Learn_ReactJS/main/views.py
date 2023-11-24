from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Learn1, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def index(request):
    # return HttpResponse("Hello, World")
    return render(request=request,
                  template_name="main/index.html",
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

def admin_home(request):
    template = "main/admin_home.html"
    students = Student.objects.all()

    context = {
        "title" : "Student",
        "students" : students
    }

    return render(request,template,context)

def admin_add_student(request):
    #template
    pass

def admin_save_student(request):
    student = Student()
    student.student_no = request.Get['student_no']
    student.firstname = request.Get['firstname']
    student.lastname = request.Get['lastname']
    student.save()

    # return HttpResponseRedirect(reverse('index'))

def funcStudentAdd(request):
    student = Student()


def funcStudentUpdate(request,id):
    student = Student.objects.get(id=id)
    student.student_no = request.Get['student_no']
    student.firstname = request.Get['firstname']
    student.lastname = request.Get['lastname']
    student.save()

def funcStudentDelete(request,id):
    student = Student(id=id)
    student.delete

    # return HttpResponseRedirect(reverse('index'))