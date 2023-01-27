from django.contrib import admin
from .models import Student,Donate


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student)
admin.site.register(Donate)