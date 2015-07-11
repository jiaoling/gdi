from django.shortcuts import render, get_object_or_404,get_list_or_404, redirect

from django.http import HttpResponse
from django.template import Context, loader
from course.models import *
from course.forms import *


def course_list(request):
    courses = Course.objects.all().order_by('start_date')
    t = loader.get_template('course_list.html')
    # added topics and instructors so the template could access names of those objects
    c = Context({'courses': courses})
    return HttpResponse(t.render(c))

def course_view(request,slug, pk):
    course = get_object_or_404(Course, pk=pk)
    material_slide = Material.objects.filter(type= 'slide', course_id = pk)
    material_code = Material.objects.filter(type= 'code', course_id = pk)
    return render(request, 'course_view.html', {'course':course,
                                                'pk':pk,
                                                'material_slide':material_slide,
                                                'material_code':material_code})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/course/')
    else:
        form = CourseForm()
    return render(request, 'add_class_form.html', {'form': form})

def edit_course(request, slug, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_view', slug=slug, pk=course_id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_class_form.html', {'form': form, 'course':course })

def delete_course(request, slug, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('/course/')
    return render(request, 'delete_class_form.html', {'course': course})