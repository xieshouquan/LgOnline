"""LgOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import os

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include

import xadmin
from django.views.generic import TemplateView
from django.views.static import serve

from LgOnline.settings import BASE_DIR
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('captcha', include('captcha.urls')),

    # 课程机构url配置
    re_path(r'^org/', include(('organization.urls', 'organization'), namespace="org")),
    url('^$', TemplateView.as_view(template_name="index.html"), name='index'),
    re_path(r'^login/', LoginView.as_view(), name='login'),
    re_path(r'^register/', RegisterView.as_view(), name='register'),
    re_path(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active'),
    re_path(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path(r'^modifypwd/$', ModifyView.as_view(), name='modify_pwd'),
    re_path(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='resetpwd'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'media')}),

]
