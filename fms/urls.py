"""fms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from company.api.views import CompanyAPIView
from fuel.api.views import FuleAPIView
from group.api.views import GroupAPIView
from jobs.api.views import JobAPIView
from users.api.views import UserLoginAPIView, UserCreateAPIView, UserAPIView
from users.views import AngularTemplateView
from vehicle.api.views import VehicleListAPIView, VehicleStatusAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^djangotemplates/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$', AngularTemplateView.as_view()),

    url(r'^api/v1/login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^api/v1/register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^api/v1/company/$', CompanyAPIView.as_view(), name='company'),
    url(r'^api/v1/vehicle/$', VehicleListAPIView.as_view(), name='vehicle'),
    url(r'^api/v1/group/$', GroupAPIView.as_view(), name='group'),

    url(r'^api/v1/user/$', UserAPIView.as_view(), name='user'),

    url(r'^api/v1/vehiclestatus/$', VehicleStatusAPIView.as_view(), name='vehiclestatus'),

    url(r'^api/v1/jobs/$', JobAPIView.as_view(), name='jobs'),
    url(r'^api/v1/fuel/$', FuleAPIView.as_view(), name='fuel'),

]
urlpatterns += [
    url(r'', TemplateView.as_view(template_name='index.html'))
]
