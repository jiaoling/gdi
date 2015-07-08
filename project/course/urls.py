__author__ = 'cjlchaos'

from django.conf.urls import patterns, url
from course import views

urlpatterns=patterns(
    'course.views',
    url(r'^$', views.course_list, name='courses'),
    url(r'^(?P<slug>\w+)-(?P<pk>\d+)/$', views.course_view, name='course_view'),
    )