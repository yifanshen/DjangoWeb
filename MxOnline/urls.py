# -*- coding: utf-8 -*-
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
#从静态文件中把view引进来
from django.views.generic import TemplateView
import  xadmin

from users.views import user_login
from users.views import LoginView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    #注意 这里根目录下 login 前面不需要加上/
    #url('^login/$', TemplateView.as_view(template_name="login.html"), name="login"),

    #这里注意，login 是传递的一个句柄， 并不要用括号考起来， 这个是6.2 6.3 对应的url
    #url('^login/$', user_login, name="login"),

    #这个是6.4 对应的 url 使用view class 来实现功能
    url('^login/$', LoginView.as_view(), name="login"),

]