from django.contrib import admin

# Register your models here.
from course.models import *

class CourseAdmin(admin.ModelAdmin):
    list_display =('c_name', 'instructor', 'level', 'start_date','end_date', 'meetup_page','topic')
admin.site.register(Course, CourseAdmin)

class MaterialAdmin(admin.ModelAdmin):
    list_display=('name', 'type', 'content')

admin.site.register(Material, MaterialAdmin)