from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from authentication.views import UserListAPIView

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django_project.views.authentication', name='authentication'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'api/v1/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
                       url(r'api/v1/users/', UserListAPIView.as_view()),
                       url(r'^.*$', TemplateView.as_view(template_name='index.html')),

                       )
