from django.contrib import admin
from course.models import *
# Register your models here.

class InstructorAdmin(admin.ModelAdmin):
    list_display =('f_name', 'l_name', 'email', 'twitter','git', 'bio','admin')
admin.site.register(Instructor, InstructorAdmin)