from django.contrib import admin
from .models import Learn1,Student
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

#customize the fields order
class AdminTinyMCETextEditor(admin.ModelAdmin):

    fieldsets=[
        ("Title/date",{"fields":["title","published"]}),
        ("Content",{"fields":["content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Learn1,AdminTinyMCETextEditor)
admin.site.register(Student)