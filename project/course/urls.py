__author__ = 'cjlchaos'

from django.conf.urls import patterns, url
from course import views
urlpatterns=patterns(
    'course.views',
    url(r'^$', views.course_list, name='courses'),
    url(r'^(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.course_view, name='course_view'),

    # url(r'^create/$', 'create_course',
    #     name="create_course"),
    url(r'^edit/(?P<slug>[-\w]+)-(?P<course_id>\d+)/$', 'edit_course',
        name='edit_course'),
    # url(r'^delete/(?P<slug>[-\w]+)-(?P<course_id>\d+)/$', 'delete_course',
    #     name='delete_course'),

    url(r'^material_create/', 'create_material',
        name='create_material'),
    url(r'^material_edit/(?P<slug>[-\w]+)-(?P<material_id>\d+)/$', 'edit_material',
        name='edit_material'),
    url(r'^material_delete/(?P<slug>[-\w]+)-(?P<material_id>\d+)/$', 'delete_material',
        name='delete_material'),
    )