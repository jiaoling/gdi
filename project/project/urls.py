from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('course.urls'), name='index'),
    url(r'^course/', include('course.urls')),
    url(r'^instructor/', include('instructor.urls')),
    url(r'^getting_started/', include('getting_started.urls')),

]
