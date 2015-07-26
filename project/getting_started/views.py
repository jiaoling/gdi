from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from course.models import *

# Create your views here.
def getting_started(request):
    courses = Course.objects.all().order_by('c_name')
    #t= loader.get_template('getting_started.html')
    #c= Context({'getting_started': courses,})
    #return HttpResponse(t.render(c))
    return render(request, 'getting_started.html', {'courses': courses})
