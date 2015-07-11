from django.shortcuts import render, get_object_or_404,get_list_or_404

from django.http import HttpResponse
from django.template import Context, loader
from course.models import Course, Instructor, Material


def course_list(request):
    courses = Course.objects.all().order_by('start_date')
    t = loader.get_template('course_list.html')
    # added topics and instructors so the template could access names of those objects
    c = Context({'courses': courses})
    return HttpResponse(t.render(c))

def course_view(request,slug, pk):
    course = get_object_or_404(Course, pk=pk)
    material_slide = get_list_or_404(Material, type= 'slide', course_id = pk)
    material_code = get_list_or_404(Material, type= 'code', course_id = pk)
    return render(request, 'course_view.html', {'course':course,
                                                'pk':pk,
                                                'material_slide':material_slide,
                                                'material_code':material_code})
def redirect_to_page(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_view.html', {'course_page':course, 'pk':pk})