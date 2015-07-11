

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import Context, loader
from course.models import Course, Instructor, Material, Topic
from instructor.forms import *
# Create your views here.

def instructor_list(request):
    instructors = Instructor.objects.all().order_by('f_name')
    t = loader.get_template('instructor_list.html')
    c = Context({'instructors': instructors,})
    return HttpResponse(t.render(c))

def instructor_view(request,slug1,slug2, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    courses = Course.objects.all().filter(instructor = pk)
    return render(request, 'instructor_view.html', {'instructor':instructor, 'courses':courses} )


def create_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/instructor/')
    else:
        form = InstructorForm()
    return render(request, 'add_instructor_form.html', {'form': form})

def edit_instructor(request, slug1, slug2, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('instructor_view', slug1=slug1, slug2=slug2, pk=instructor_id)
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'edit_instructor_form.html', {'form': form, 'instructor':instructor })

def delete_instructor(request, slug1,slug2, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        instructor.delete()
        return redirect('/instructor/')
    return render(request, 'delete_instructor_form.html', {'instructor': instructor})