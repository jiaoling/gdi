__author__ = 'cjlchaos'

from django.conf.urls import patterns, url
from course import views
urlpatterns=patterns(
    'course.views',
    url(r'^$', views.course_list, name='courses'),
    url(r'^(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.course_view, name='course_view'),

    # url(r'^create/$', 'create_course',
    #     name="create_course"),
    url(r'^(?P<slug>[-\w]+)-(?P<course_id>\d+)/edit/$', 'edit_course',
        name='edit_course'),
    # url(r'^delete/(?P<slug>[-\w]+)-(?P<course_id>\d+)/$', 'delete_course',
    #     name='delete_course'),

    url(r'^(?P<slug>[-\w]+)-(?P<course_id>\d+)/material_create/$', 'create_material',
        name='create_material'),
    url(r'^(?P<slug1>[-\w]+)-(?P<course_id>\d+)/(?P<slug2>[-\w]+)-(?P<material_id>\d+)/material_edit/$', 'edit_material',
        name='edit_material'),
    url(r'^(?P<slug1>[-\w]+)-(?P<course_id>\d+)/(?P<slug2>[-\w]+)-(?P<material_id>\d+)/material_delete/$', 'delete_material',
        name='delete_material'),
    )