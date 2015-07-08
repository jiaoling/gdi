__author__ = 'cjlchaos'
from django.conf.urls import patterns, url
from getting_started import views

urlpatterns = patterns(
    'getting_started.views',
    url(r'$', views.getting_started, name = 'getting_started'),
)

