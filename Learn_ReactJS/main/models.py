from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password

# Model django documentation.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/

class Account(models.Model):
    #id is auto-generated
    account_type = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    ]
    id = models.IntegerField('ID','id',primary_key=True)
    username = models.CharField("Username","username",max_length=200,default="username", unique=True)
    firstname = models.CharField("First Name","firstname",max_length=200,default="firstname")
    lastname = models.CharField("Last Name","lastname",max_length=200,default="lastname")
    email = models.CharField("Email","email",max_length=200,default="email", unique=True)
    password = models.CharField("Password","password",max_length=200,default="password", help_text="Be Careful on changing passwords directly from the admin site, make sure to input the plain text password! Do not save if will the password not being in plain text or else it will be set to the current value(encrypted) and not as intended")
    type = models.CharField("Account Type", 'type', max_length=20,choices=account_type)
    image = models.ImageField(upload_to="thumbnails",default='media/thumbnails/user-default.png')
    
    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

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
    def __str__(self) -> str:
        return self.title
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
    title = models.CharField(max_length=255)
    lesson = models.ForeignKey(Learn1, on_delete=models.CASCADE)
    # questions and answers
    # unit scope? 
    # pass
    def __str__(self):
        return self.title

class Quiz(models.Model):
    #id
    #fk lesson_id, which lesson it belongs
    # questions and answers
    title = models.CharField(max_length=255)
    lesson = models.ForeignKey(Learn1, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    # pass

class Quiz_Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    choices = models.JSONField()
    correct_choice = models.CharField(max_length=1)
    def __str__(self):
        return f"{self.quiz.title} - Question {self.pk}: {self.question_text}"
    
class Assessment_Question(models.Model):
    exam = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question_text = models.TextField()
    choices = models.JSONField()
    correct_choice = models.CharField(max_length=1)
    def __str__(self):
        return f"{self.quiz.title} - Question {self.pk}: {self.question_text}"
    
class Badge(models.Model):
    image = models.ImageField(upload_to='{% static "main/assets/badges" %}')
    name = models.CharField(max_length=255)
    requirements = models.TextField()
    def __str__(self) -> str:
        return self.name