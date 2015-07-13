__author__ = 'cjlchaos'
from django import forms
from course.models import *
from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        # uncomment the below line to include only specific fields
        # fields = ('c_name', 'description')

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ('f_name', 'l_name', 'bio','git','twitter', 'admin','admin','pic')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')