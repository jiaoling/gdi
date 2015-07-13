from django.shortcuts import render, get_object_or_404,get_list_or_404, redirect

from django.http import HttpResponse
from django.template import Context, loader
from course.models import *
from course.forms import *
from slugify import slugify


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

# course
# def create_course(request):
#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/course/')
#     else:
#         form = CourseForm()
#     return render(request, 'course_form/add_class_form.html', {'form': form})

def edit_course(request, slug, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_view', slug=slug, pk=course_id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form/edit_class_form.html', {'form': form, 'course':course })

# def delete_course(request, slug, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     if request.method == 'POST':
#         course.delete()
#         return redirect('/course/')
#     return render(request, 'course_form/delete_class_form.html', {'course': course})

#material
def create_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/course/')
    else:
        form = MaterialForm()
    return render(request, 'material_form/add_material_form.html', {'form': form})

def edit_material(request,slug, material_id):
    material = get_object_or_404(Material, pk=material_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST,request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('course_view', slug=slugify(material.course.c_name), pk=material.course.pk)
    else:
        form = MaterialForm(instance=material)
    return render(request, 'material_form/edit_material_form.html', {'form': form, 'material':material })

def delete_material(request, slug, material_id):
    material = get_object_or_404(Material, pk=material_id)
    if request.method == 'POST':
        material.delete()
        return redirect('/course/')
    return render(request, 'material_form/delete_material_form.html', {'material': material})
