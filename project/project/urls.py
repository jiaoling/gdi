from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from project import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^course/', include('course.urls')),
    url(r'^login/', views.user_login, name='login'),
    url(r'^instructor/', include('instructor.urls')),
    url(r'^getting_started/', include('getting_started.urls')),
    # url(r'^register/', views.register, name='register'),

    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/', views.user_logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
