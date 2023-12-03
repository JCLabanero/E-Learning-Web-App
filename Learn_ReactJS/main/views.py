from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Learn1, Student, Account, Quiz, Quiz_Question, Assessment, Assessment_Question, Badge
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
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f"New account created: {username}")
    #         # login(request,user)
    #         return redirect("main:login")
    #     else:
    #         for fields in form:
    #             for error in fields.errors:
    #                 messages.error(request,f"{fields.label}: {error}")
    #         return render(
    #         request,
    #         "main/register.html",
    #         context={"form": form}
    #         )
    # form = UserCreationForm
    # return render(request,
    #             "main/register.html",
    #             context={"form":form})
    if request.method == 'POST':
        account = Account()
        account.username = request.POST['username']
        account.password = request.POST['password']
        account.firstname = request.POST['firstname']
        account.lastname = request.POST['lastname']
        account.email = request.POST['email']
        account.account_type = request.POST['type']
        account.image = request.FILES['userImage']
        account.save()

    return render(request, 'main/index.html')

def admin_home(request):
    template = "main/admin/index.html"
    students = Student.objects.all()

    context = {
        "title" : "Student",
        "students" : students
    }

    return render(request,template,context)

def astudentlist(request):
    return render(request, 'main/admin/students.html', {'students': Student.objects.all()})

def astudentinfo(request,pk):
    student = get_object_or_404(Student,pk=pk)
    return render(request,'main/admin/student_info.html',{'student':student})

def astudentnew(request):
    #template
    if request.method == "POST":
        form = Student(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('main:a')
    else:
        form = Student()
    return render(request,'main/admin/student_new.html',{'form':form})
    # student = Student()
    pass

def astudentedit(request):
    # render html editor
    pass

def astudentdelete(request):
    # confirmation?
    pass

def funcStudentNew(request):
    if request.method=="POST":
        form = Student(request.POST)
    student = Student()
    student.student_no = request.Get['student_no']
    student.firstname = request.Get['firstname']
    student.lastname = request.Get['lastname']
    student.save()

    # return HttpResponseRedirect(reverse('index'))

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

def funcLessonList(request):
    template = 'main/admin/lesson.html'
    context = {
        "lessons": Learn1.objects.all()
    }
    return render(request, template, context)

def funcLoadLesson(request, id):
    template = 'main/admin/viewLesson.html' 
    context = {
        "lessons": Learn1.objects.all(),
        "lesson": Learn1.objects.get(id=id)
    }
    return render(request, template, context)

def alessonList(request):
    #replace obj with lesson
    return render(request, 'main/admin/lesson.html', {'lesson': Student.objects.all()})

def aAssessments(request):
    return render(request, 'main/admin/assessments.html', {'assessment': Student.objects.all()})

def aAchievements(request):
    return render(request, 'main/admin/achievements.html', {'achievements': Student.objects.all()})

def aReports(request):
    return render(request, 'main/admin/reports.html', {'reports': Student.objects.all()})

def aLogs(request):
    return render(request, 'main/admin/activityLogs.html', {'logs': Student.objects.all()})

def aOpenLesson(request):
    return render(request, 'main/admin/viewLesson.html', {'logs': Student.objects.all()})

def aLessonEditor(request):
    return render(request, 'main/admin/lessonEditor.html', {'logs': Student.objects.all()})

def profile(request):
    return render(request, 'main/myprofile.html', {'logs': Student.objects.all()})
