# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import  authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile

# Create your views here.

# 6.3 ->|
class CustomBackend(ModelBackend):
    #这个函数是用来定制化登录功能的 就是在user_Login的那个authenticate的函数的改写
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            #用Q就可以执行or操作
            print "log correctly"
            user = UserProfile.objects.get(Q(username = username)|Q(email = username))
            if user.check_password(password):
                print "password is correct"
                return user
            else:
                print "password is wrong"
        except Exception as e:
            print "log fail"
            return None


# 6.2 ->|
def user_login(request):
    #post 用来处理用户名 密码的输入
    if request.method == "POST":
        #后面的那个参数为默认值
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        #这边会对用户名和密码进行验证， 如果正确会返回一个model 否则是none
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            #login  这个函数自动会把user 写进request中
            print "user_login log correctly"
            login(request, user)
            return render(request, "index.html")#目前还没有dashboard 先渲染主页面
        else:
            #没有登录成功就继续留在登录页面上面
            print "user_login log fail"
            return render(request, "login.html", {"msg":"username or password wrong"})
    #get用来处理login 页面的请求
    elif request.method == "GET":
        #如果用户是请求的get 那么我们就返回一个render第一个参数是request， 第二个是需要渲染的页面，的三个是用来传递参数的dic
        return render(request, "login.html", {})

#6.4 ->| 和前面两个章节的功能类似，不过前面是通过函数修改的方法来实现功能，而这个章节是通过类的改修来实现功能
class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})
    def post(self, request):
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        # 这边会对用户名和密码进行验证， 如果正确会返回一个model 否则是none
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            # login  这个函数自动会把user 写进request中
            print "user_login log correctly"
            login(request, user)
            return render(request, "index.html")  # 目前还没有dashboard 先渲染主页面
        else:
            # 没有登录成功就继续留在登录页面上面
            print "user_login log fail"
            return render(request, "login.html", {"msg": "username or password wrong"})
