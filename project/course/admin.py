from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from course.models import *

class CourseAdmin(admin.ModelAdmin):
    list_display =('c_name', 'instructor', 'level', 'start_date','end_date', 'meetup_page','topic')
admin.site.register(Course, CourseAdmin)

class InstructorInline(admin.StackedInline):
	model = Instructor

class UserAdmin(UserAdmin):
	inlines = (InstructorInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
