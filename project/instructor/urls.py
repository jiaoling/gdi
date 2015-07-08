__author__ = 'cjlchaos'


from django.conf.urls import patterns, url
from instructor import views

urlpatterns=patterns(
    'instructor.views',
    url(r'^$', views.instructor_list, name='instructors'),
    url(r'^(?P<slug>[-\w\d]+),(?P<pk>\d+)/$', views.instructor_view)
    )