from django.contrib import admin
from .models import Learn1,Student,Badge,Quiz,Quiz_Question,Assessment,Assessment_Question,Account
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

#customize the fields order
class AdminTinyMCETextEditor(admin.ModelAdmin):

    fieldsets=[
        ("Unit No.",{"fields":['unitNo']}),
        ("Lesson No.",{"fields":['lessonNo']}),
        ("Title/date",{"fields":["title","published"]}),
        ("Content",{"fields":["content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Learn1,AdminTinyMCETextEditor)
admin.site.register(Student)
admin.site.register(Badge)
admin.site.register(Quiz)
admin.site.register(Quiz_Question)
admin.site.register(Assessment)
admin.site.register(Assessment_Question)
admin.site.register(Account)