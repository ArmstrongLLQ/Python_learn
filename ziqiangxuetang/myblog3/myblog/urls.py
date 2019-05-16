"""myblog URL Configuration

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
from django.urls import path, re_path
from django.views import static
from django.conf import settings
from blog.upload import upload_image
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    re_path(r"^uploads/(?P<path>.*)$", static.serve,{"document_root": settings.MEDIA_ROOT, }),
    re_path(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    path('archive/', archive, name='archive'),
    path('article/', article, name='article'),
    path('comment/post/', comment_post, name='comment_post'),
    path('logout', do_logout, name='logout'),
    path('reg', do_reg, name='reg'),
    path('login', do_login, name='login'),
    path('category/', category, name='category'),
]
