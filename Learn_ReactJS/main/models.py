from django.db import models
from datetime import datetime

# Create your models here.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/

#python models command
## for changes/updates/creates
#python manage.py makemigrations

## migrate to other db?
#python manage.py sqlmigrate main 0001

#pyton manage.py migrate

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

class Learn1(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.title

class Unit(models.Model):
    #id
    #title
    #holds lesson in it
    pass

class Lesson(models.Model):
    #id
    #fk instructor, who created this lesson, might not be necessary

    #unit number
    pass

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