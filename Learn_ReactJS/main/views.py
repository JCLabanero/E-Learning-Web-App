from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Learn1, Student, Account, Quiz, Quiz_Question, Assessment, Assessment_Question, Badge
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.urls import reverse
import sweetify
from django.contrib.auth.decorators import login_required
import time
from functools import wraps

# Create your views here.

def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('id') and not request.session.get('username') and not request.session.get('password') and not request.session.get('type'):
            return redirect('/')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def logout(request):
    request.session.clear()
    return redirect('/')

def setSession(request, username):
    user = Account.objects.get(username=username)
    request.session['id'] = user.id
    request.session['username'] = user.username
    request.session['password'] = user.password
    request.session['imagePath'] = user.image.url
    if(user.type == 'Teacher'):
        request.session['type'] = 'a'
    elif(user.type == 'Student'):
        request.session['type'] = 'u'

#add this decorator to pages that requires log-in
@login_required
def dashboard(request):
    # return HttpResponse("Hello, World")
    return render(request=request,
                  template_name="main/index.html",context={"Learn1":Learn1.objects.all,})

def login(request):
    return render(request, 'main/login.html')
    # return render(request=request,template_name="main/login.html")

def login_submit(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Account.objects.get(username=username)
            if check_password(password, user.password):
                setSession(request, username)
                return redirect('main:dashboard')

            else:
                sweetify.toast(request, title="Invalid Account!", icon='error', timer=3000, position='top')
                return redirect('/')
        except Account.DoesNotExist:
            sweetify.toast(request, title='Invalid Account!', icon='error', timer=3000, position='top')
            return redirect('/')
    else:
        return redirect('/')
    
def register(request, username=None):
    # code to check if uniques values exist
    if request.method == 'POST':
        username_exists = Account.objects.filter(username=request.POST['username']).exists()
        email_exists = Account.objects.filter(email=request.POST['email']).exists()

        if username_exists or email_exists:
            sweetify.toast(request, title='Duplicate Username or Email', icon='error', timer=3000, position='top')
            return redirect('/')
        
        account = Account()
        account.username = request.POST['username']
        account.password = request.POST['password']
        account.firstname = request.POST['firstname']
        account.lastname = request.POST['lastname']
        account.email = request.POST['email']
        account.type = request.POST['account_type']
        account.image = request.FILES['userImage']

        account.save()
        sweetify.toast(request, title='Account Registered', icon='success', timer=3000, position='top')
        # time.sleep(1)
        setSession(request, account.username)

        return redirect('main:dashboard')

def admin_home(request):
    template = "main/admin/index.html"
    students = Student.objects.all()

    context = {
        "title" : "Student",
        "students" : students
    }

    return render(request,template,context)

@login_required
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
    return render(request, 'main/admin/viewLesson.html', {'lesson': Student.objects.all()})

def aLessonEditor(request, id):
    return render(request, 'main/admin/lessonEditor.html', {
        "lessons": Learn1.objects.all(),
        'lesson': Learn1.objects.get(id=id)})

def profile(request, id=1):
    return render(request, 'main/myprofile.html', {'account': Account.objects.all()})
