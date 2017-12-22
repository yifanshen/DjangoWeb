# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"nichen", default= "")
    birthday =models.DateTimeField(verbose_name=u"shengri", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male",u"nan"),("female",u"nv")), default="female")
    address = models.CharField(max_length=100, default=u"unknow")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"yonghuxinxi"
        verbose_name_plural = verbose_name


    # 设定返回的信息
    def __unicode__(self):
        return self.username

# 4-4 ->

#邮箱验证使用
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"yanzhengma")
    email = models.EmailField(max_length=50, verbose_name=u"youxiang")
    send_type = models.CharField(verbose_name=u"yanzhengmaleixing",choices=(("register",u"zhuce"),("forget", u"zhaohuimima")), max_length=10)
    send_time = models.DateTimeField(verbose_name=u"fasongshijian",default=datetime.now)

    class Meta:
        verbose_name = u"youxiangyanzhengma"
        verbose_name_plural = verbose_name



    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

#首页图片轮播部分
class Banne(models.Model):
    titile = models.CharField(max_length=100, verbose_name=u"biaoti")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"lunbotu", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"fangwendizhi")
    index = models.IntegerField(default=100, verbose_name=u"shunxu")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"fangwenshijian")

    class Meta:
        verbose_name = u"lunbotu"
        verbose_name_plural = verbose_name

# <- 4.4