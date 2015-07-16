
__author__ = 'cjlchaos'


from django.conf.urls import patterns, url
from instructor import views



urlpatterns=patterns(
    'instructor.views',
    url(r'^$', views.instructor_list, name='instructors'),
    url(r'^(?P<slug1>[-\w]+)-(?P<slug2>[-\w]+)-(?P<pk>\d+)/$','instructor_view', name='instructor_view'),

    # url(r'^(?P<slug1>[-\w]+)-(?P<slug2>[-\w]+)-(?P<instructor_id>\d+)/create/$', 'create_instructor',
    #     name="create_instructor"),
    url(r'^(?P<slug1>[-\w]+)-(?P<slug2>[-\w]+)-(?P<instructor_id>\d+)/edit/$', 'edit_instructor',
        name='edit_instructor'),
    # url(r'^(?P<slug1>[-\w]+)-(?P<slug2>[-\w]+)-(?P<instructor_id>\d+)/delete/$', 'delete_instructor',
    #     name='delete_instructor'),
    )
