from django.db import models
from datetime import datetime

# Create your models here.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/

#python models command
## for changes/updates/creates
#python manage.py makemigrations

## migrate to other db?
#python manage.py sqlmigrate main 0001

#python manage.py migrate

## 
# python manage.py shell
# cmd 
# > from main.models import Learn1
# > from django.utils import timezone 
# > Learn1.objects.all()
# > new_learn1 = Learn1(title="To be", content="...or not to be", published=timezone.now())
# > new_learn1.save()
# > Learn1.objects.all() 
# > for t in Learn1.objects.all():
# >     print(t.title)
# > exit() 

class Student(models.Model):
    student_no = models.IntegerField("Student No.","student_no",primary_key=True,unique=True)
    firstname = models.CharField("First Name","firstname",max_length=200,default="firstname")
    lastname = models.CharField("Last Name","lastname",max_length=200,default="lastname")
    email = models.CharField("Email","email",max_length=200,default="email")

class Learn1(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default="The content of the lesson should go here.")
    published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.title

class Unit(models.Model):
    unit_no = models.IntegerField("Unit No.","unit_no",default=1)
    title = models.CharField("Name","name",max_length=200)
    #id
    #holds lesson in it
    pass

class Lesson(models.Model):
    #id auto generated
    title = models.CharField("Title","title",max_length=200,default="Title here")
    content = models.TextField("Content","content",default="The content of the lesson should go here.")
    # unit_no = models.IntegerField(max_length=20,verbose_name="Lesson No.", name="lesson_no")
    published = models.DateTimeField("date published", default=datetime.now())

    unit_no = models.ForeignKey(Unit, on_delete=models.CASCADE,default=0)

    def __str__(self) -> str:
        return self.title
    #fk instructor, who created this lesson, might not be necessary

    #unit number

class Assessment(models.Model):
    #id
    #fk lesson_id, which lesson it belongs
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    # questions and answers
    # unit scope? 
    pass

class Quizzes(models.Model):
    #id
    #fk lesson_id, which lesson it belongs
    # questions and answers
    pass
