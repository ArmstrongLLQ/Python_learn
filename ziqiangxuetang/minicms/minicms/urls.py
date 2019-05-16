"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from news.upload import upload_image
from news.views import *
from django.views import static
from django.conf import settings

import os


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    re_path(r"^uploads/(?P<path>.*)$", static.serve,{"document_root": settings.MEDIA_ROOT, }),

    path('', index, name='index'),
    path('cloumn/<slug:slug>/', column_detail, name='column'),
    path('news/<slug:slug>/', article_detail, name='article'),
]
