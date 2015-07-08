

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from course.models import Course, Instructor, Material, Topic
# Create your views here.

def instructor_list(request):
    instructors = Instructor.objects.all().order_by('f_name')
    t = loader.get_template('instructor_list.html')
    c = Context({'instructors': instructors,})
    return HttpResponse(t.render(c))

def instructor_view(request,slug, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    courses = Course.objects.all().filter(instructor = pk)
    return render(request, 'instructor_view.html', {'instructor':instructor, 'courses':courses} )