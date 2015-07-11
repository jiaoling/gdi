__author__ = 'cjlchaos'


from django.conf.urls import patterns, url
from instructor import views

urlpatterns=patterns(
    'instructor.views',
    url(r'^$', views.instructor_list, name='instructors'),
<<<<<<< HEAD
    url(r'^(?P<slug>[-\w\d]+),(?P<pk>\d+)/$', views.instructor_view)
=======
    url(r'^(?P<slug1>[-\w]+)-(?P<slug2>[-\w]+)-(?P<pk>\d+)/$', views.instructor_view),
    url(r'^create/$', 'create_instructor',
        name="create_instructor"),
    url(r'^edit/(?P<slug1>[-\w]+)-(?P<slug2>[-\w]+)-(?P<instructor_id>\d+)/$', 'edit_instructor',
        name='edit_instructor'),
    url(r'^delete/(?P<slug1>[-\w]+)-(?P<slug2>[-\w]+)-(?P<instructor_idk>\d+)/$', 'delete_instructor',
        name='delete_instructor'),
>>>>>>> july_11th_branch
    )