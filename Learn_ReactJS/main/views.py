from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.db import *
from .models import Learn1, Student, Account, Quiz, Quiz_Question, Assessment, Assessment_Question, Badge
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from functools import wraps
import sweetify
from django.db.models import Count
import random
import time

# Create your views here.
def units():
    lessons = Learn1.objects.all()
    units = sorted(set(lesson.unitNo for lesson in lessons))
    return units

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

def setSession(request, id, password):
    request.session.clear()
    user = Account.objects.get(id=id)
    request.session['id'] = user.id
    request.session['username'] = user.username
    request.session['password'] = password
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
                setSession(request, user.id, password)
                return redirect('main:dashboard')

            else:
                sweetify.toast(request, title="Invalid Account!", icon='error', timer=3000, position='top')
                return redirect('/')
        except Account.DoesNotExist:
            sweetify.toast(request, title='Invalid Account!', icon='error', timer=3000, position='top')
            return redirect('/')
    else:
        return redirect('/')
    
def register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            if Account.objects.filter(username=username).exists():
                sweetify.toast(request, title='Duplicate Username or Email', icon='error', timer=3000, position='top')
                return render(request, 'registration.html', {'error': 'Username already exists'})

            if Account.objects.filter(email=email).exists():
                sweetify.toast(request, title='Duplicate Username or Email', icon='error', timer=3000, position='top')
                return render(request, 'registration.html', {'error': 'Email already exists'})
            else:
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
                # Authenticate the user after successfully creating the account
                return redirect('main:login')
    except Exception as e:
        # Handle exceptions (e.g., print or log the error)
        print(f"An error occurred: {str(e)}")

    return redirect('/')
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
    lessons = Learn1.objects.all().order_by('lessonNo')
    return render(request, 'main/admin/lesson.html', {
        # create obj for units
        'units': units,
        'lessons': lessons
        })

def funcLoadLesson(request, id):
    template = 'main/admin/viewLesson.html' 
    context = {
        "units": units(),
        "lessons": Learn1.objects.all(),
        "lesson": Learn1.objects.get(id=id)
    }
    return render(request, template, context)

def aAssessments(request):
    return render(request, 'main/admin/assessments.html', {'quizzes': Quiz.objects.all(), 'exams':Assessment.objects.all()})
def assessmentDelete(request, id):
    try:
        quiz = Quiz.objects.get(id=id)
    except:
        quiz = Assessment.objects.get(id=id)
    sweetify.toast(request, title='Assessment Deleted!', icon='success', timer=3000, position='top')
    quiz.delete()
    return render(request, 'main/admin/assessments.html', {'quizzes': Quiz.objects.all(), 'exams':Assessment.objects.all()})

def assessmentCreate(request, type):
    try:
        if request.method == "POST":
            if type == 'quiz':
                x = 11
                quiz = Quiz()
                quiz.title = request.POST.get('assessmentTitle', '')
                quiz.lesson = request.POST.get('assessmentRef', '')
                quiz.save()
                for x in range(1, x):
                    quizQ = Quiz_Question()
                    quizQ.quiz = quiz
                    quizQ.question_text = request.POST.get(f'question{x}')
                    quizQ.optionA = request.POST.get(f'option{x}A')
                    quizQ.optionB = request.POST.get(f'option{x}B')
                    quizQ.optionC = request.POST.get(f'option{x}C')
                    quizQ.optionD = request.POST.get(f'option{x}D')
                    quizQ.correct_choice = request.POST.get(f'correctAnswer{x}')
                    quizQ.save()
                sweetify.toast(request, title='Quiz Added', icon='success', timer=3000, position='top')
                return render(request, 'main/admin/assessments.html', {'quizzes': Quiz.objects.all(), 'exams': Assessment.objects.all(), 'type': type, 'lessons': Learn1.objects.all()})
            elif type == 'exam':
                x = 16
                quiz = Assessment()
                quiz.title = request.POST.get('assessmentTitle', '')
                quiz.lesson = request.POST.get('assessmentRef', '')
                quiz.save()
                for x in range(1, x):
                    quizQ = Assessment_Question()
                    quizQ.exam = quiz
                    quizQ.question_text = request.POST.get(f'question{x}')
                    quizQ.optionA = request.POST.get(f'option{x}A')
                    quizQ.optionB = request.POST.get(f'option{x}B')
                    quizQ.optionC = request.POST.get(f'option{x}C')
                    quizQ.optionD = request.POST.get(f'option{x}D')
                    quizQ.correct_choice = request.POST.get(f'correctAnswer{x}')
                    quizQ.save()
                sweetify.toast(request, title='Exam Added', icon='success', timer=3000, position='top')
                return render(request, 'main/admin/assessments.html', {'quizzes': Quiz.objects.all(), 'exams': Assessment.objects.all(), 'type': type, 'lessons': Learn1.objects.all()})
        else:
            return render(request, 'main/admin/createAssessment.html', {'quizzes': Quiz.objects.all(), 'exams': Assessment.objects.all(), 'type': type, 'lessons': Learn1.objects.all()})
    except Exception as e:
        sweetify.toast(request, title='Error creating assessment', icon='error', timer=3000, position='top')
        return e

def assessmentEdit(request,type,id):
    if type == 'quiz':
        quiz_instance = Quiz_Question.objects.filter(quiz=Quiz.objects.get(id=id))
    else:
        exam_instance = Assessment_Question.objects.filter(exam=Assessment.objects.get(id=id))
    if request.method == "POST":
            if type == 'quiz':
                x = 1
                quiz = Quiz.objects.get(id=id)
                quiz.title = request.POST.get('assessmentTitle', '')
                quiz.lesson = request.POST.get('assessmentRef', '')
                quiz.save()

                quiz_questions = Quiz_Question.objects.filter(quiz=quiz)
                for quizQ in quiz_questions:
                    quizQ.question_text = request.POST.get(f'question{x}')
                    quizQ.optionA = request.POST.get(f'option{x}A')
                    quizQ.optionB = request.POST.get(f'option{x}B')
                    quizQ.optionC = request.POST.get(f'option{x}C')
                    quizQ.optionD = request.POST.get(f'option{x}D')
                    quizQ.correct_choice = request.POST.get(f'correctAnswer{x}')
                    quizQ.save()
                    x+=1

            elif type == 'exam':
                x = 1
                exam = Assessment.objects.get(id=id)
                exam.title = request.POST.get('assessmentTitle','')
                exam.lesson = request.POST.get('assessmentRef','')
                quiz_questions = Assessment_Question.objects.filter(exam=exam)
                for quizQ in quiz_questions:
                    quizQ.question_text = request.POST.get(f'question{x}')
                    quizQ.optionA = request.POST.get(f'option{x}A')
                    quizQ.optionB = request.POST.get(f'option{x}B')
                    quizQ.optionC = request.POST.get(f'option{x}C')
                    quizQ.optionD = request.POST.get(f'option{x}D')
                    quizQ.correct_choice = request.POST.get(f'correctAnswer{x}')
                    quizQ.save()
                    x+=1
            sweetify.toast(request, title='Assessment Updated!', icon='success', timer=3000, position='top')
            return render(request, 'main/admin/assessments.html', {'quizzes': Quiz.objects.all(), 'exams': Assessment.objects.all()})
    if type == 'quiz':
        return render(request, 'main/admin/editAssessment.html', {'quiz': Quiz.objects.get(id=id),'type':type, 'quizzes_question': quiz_instance})
    elif type == 'exam':
        return render(request, 'main/admin/editAssessment.html', {'quiz': Assessment.objects.get(id=id),'type':type, 'quizzes_question': exam_instance})

def aAchievements(request):
    return render(request, 'main/admin/achievements.html', {'achievements': Student.objects.all()})

def aReports(request):
    return render(request, 'main/admin/reports.html', {'reports': Student.objects.all()})

def aLogs(request):
    return render(request, 'main/admin/activityLogs.html', {'logs': Student.objects.all()})

def aOpenLesson(request):
    return render(request, 'main/admin/viewLesson.html', {'lesson': Student.objects.all()})
    
def createLesson(request, unit):
    try:
        if request.method == 'POST':
            lesson = Learn1()
            lesson.title = request.POST['title']
            lesson.unitNo = request.POST['unitNo']
            lesson.lessonNo = request.POST['lessonNo']
            lesson.content = request.POST['content']
            lesson.save()
            sweetify.toast(request, title='Lesson Created!', icon='success', timer=3000, position='top')
            return redirect('main:lesson')
        else:
            return render(request, "main/admin/lessonCreator.html",{
                "units": units(),
                "lessons": Learn1.objects.all().order_by('lessonNo'),
                "currUnit": unit
            })
    except IntegrityError:
        sweetify.toast(request, title='Lesson Number already Exist!', icon='error', timer=3000, position='top')
        pass
    except:
        sweetify.toast(request, title='Error creating lesson!', icon='error', timer=3000, position='top')

def updateLesson(request, id):
    try:
        if request.method == 'POST':
            lesson = Learn1.objects.get(id=id)
            lesson.title = request.POST['title']
            # lesson.unitNo = lesson.unitNo
            # lesson.lessonNo = lesson.lessonNo
            lesson.content = request.POST['updatedContent']
            lesson.save()
            sweetify.toast(request, title='Lesson Updated!', icon='success', timer=3000, position='top')
        else:
            return render(request, 'main/admin/lessonEditor.html', {
            "units": units(),
            "lessons": Learn1.objects.all().order_by('lessonNo'),
            'lesson': Learn1.objects.get(id=id)})

    except:
        sweetify.toast(request, title='Error updating lesson!', icon='error', timer=3000, position='top')
        pass
    return redirect('main:lesson')

def deleteLesson(request, id):
    try:
        # sweetify.warning(request, 'Are you sure you want to delete this?', persistent="YES")
        if request.method == 'GET':
            lesson = Learn1.objects.get(id=id)
            lesson.delete()
            sweetify.toast(request, title='Lesson Deleted!', icon='success', timer=3000, position='top')
    except Exception as e:
        sweetify.toast(request, title='Error updating lesson!', icon='error', timer=3000, position='top')
    return redirect('main:lesson')

def deleteUnit(request, unit):
    try:
        # sweetify.warning(request, 'Are you sure you want to delete this?', persistent="YES")
        if request.method == 'GET':
            unit = Learn1.objects.filter(unitNo=unit)
            unit.delete()
            sweetify.toast(request, title='Unit Deleted!', icon='success', timer=3000, position='top')
    except Exception as e:
        sweetify.toast(request, title='Error deleting unit!', icon='error', timer=3000, position='top')
    return redirect('main:lesson')

def profile(request, id):
    try:
        if request.method == "POST":
            account = Account.objects.get(id=id)
            
            if account.username != request.POST.get('username', '') and Account.objects.filter(username=request.POST.get('username', '')).exists():
                sweetify.toast(request, title='Username already in use', icon='error', timer=3000, position='top')
                return render(request, 'main/myprofile.html', {'account': Account.objects.get(id=id)})
            
            if account.email != request.POST.get('email', '') and Account.objects.filter(email=request.POST.get('email', '')).exists():
                sweetify.toast(request, title='E-mail already in use', icon='error', timer=3000, position='top')
                return render(request, 'main/myprofile.html', {'account': Account.objects.get(id=id)})
            
            account.username = request.POST.get('username', '')
            account.password = request.POST.get('password', '')
            account.firstname = request.POST.get('firstname', '')
            account.lastname = request.POST.get('lastname', '')
            account.email = request.POST.get('email', '')
            if 'userImage' in request.FILES:
                account.image = request.FILES['userImage']
            account.save()
            setSession(request, id, request.POST.get('password', ''))
            sweetify.toast(request, title='Profile updated!', icon='success', timer=3000, position='top')
            return redirect('main:profile', id=id)
    except Exception as e:
        sweetify.toast(request, title='Error updating profile!', icon='error', timer=3000, position='top')
        # return redirect('main:profile', id=id)
        return e
    return render(request, 'main/myprofile.html', {'account': Account.objects.get(id=id)})

def deleteProfile(request, id):
    try:
        if request.method == 'GET':
            user = Account.objects.get(id=id)
            user.delete()
            sweetify.sweetalert(request, title='Account Deleted!', text="You will be redirected to the log-in page.", icon='success', persistent="OK", position='top')
    except Exception as e:
        sweetify.toast(request, title='Error updating lesson!', icon='error', timer=3000, position='top')
    return redirect('/')

def index(request):
    return render(request,'main/frontpage.html')
    pass

def studentTakeQuiz(request, type, id):
    if type == 'quiz':
        x = 3
        total_questions = Quiz_Question.objects.filter(quiz=id).count()
        if total_questions >= 3:
            random_indices = random.sample(range(1, total_questions), x)
            questions = Quiz_Question.objects.filter(quiz=id).order_by('id')[random_indices[0]:random_indices[0]+x]
        else:
            questions = Quiz_Question.objects.filter(quiz=id)
    elif type == 'exam':
        x = 5
        total_questions = Assessment_Question.objects.filter(exam=id).count()
        if total_questions >= 3:
            random_indices = random.sample(range(1, total_questions), x)
            questions = Assessment_Question.objects.filter(exam=id).order_by('id')[random_indices[0]:random_indices[0]+x]
        else:
            questions = Assessment_Question.objects.filter(exam=id)
    return render(request, 'main/admin/student_takequiz.html', {'questions': questions, 'type':type, 'id':id})

def result(request, type, id):
    score = 0
    if request.method == "POST":
        x = 1
        if type == 'quiz':
            while x <= 3:
                set = Quiz_Question.objects.get(id=request.POST.get(f'Q{x}ID',''))
                if set.correct_choice == request.POST.get(f'A{x}',''):
                    score+=1
                x+=1
            finalScore = f'{(score * 100/3):.2f}'
            if float(finalScore) >= 75.00:
                sweetify.sweetalert(request, title='You Passed!',text=finalScore+'%', icon='success', persistent="OK")
            else:
                sweetify.sweetalert(request, title='You Failed!',text=finalScore+'%', icon='error', persistent="OK")
        elif type == 'exam':
            while x <= 3:
                set = Assessment_Question.objects.get(id=request.POST.get(f'Q{x}ID',''))
                if set.correct_choice == request.POST.get(f'A{x}',''):
                    score+=1
                x+=1
            finalScore = f'{(score * 100/5):.2f}'
            if float(finalScore) >= 75.00:
                sweetify.sweetalert(request, title='You Passed!',text=finalScore+'%', icon='success', persistent="OK")
            else:
                sweetify.sweetalert(request, title='You Failed!',text=finalScore+'%', icon='error', persistent="OK")
        return redirect('main:assessments')
    

