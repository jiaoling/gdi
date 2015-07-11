__author__ = 'cjlchaos'
from django import forms
from course.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        # uncomment the below line to include only specific fields
        # fields = ('c_name', 'description')

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'