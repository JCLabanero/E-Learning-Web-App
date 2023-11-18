from django.contrib import admin
from .models import Learn1

# Register your models here.

#customize the fields order
class Learn1Admin(admin.ModelAdmin):
    # fields = ["title",
    # "published",
    # "content",
    # ]

    fieldsets=[
        ("Title/date",{"fields":["title","published"]}),
        ("Content",{"fields":["content"]})
    ]

admin.site.register(Learn1,Learn1Admin)