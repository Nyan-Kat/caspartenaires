"""caspartenaires URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
#-*- coding: utf8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_redirect, name='login_redirect'),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}),
    url(r'^contrat/', include('contrat.urls', namespace='contrat', app_name='contrat')),
    url(r'^administration/', include('administration.urls', namespace='administration', app_name='administration')),
]

