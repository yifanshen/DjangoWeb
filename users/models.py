# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"nichen", default= "")
    birthday =models.DateTimeField(verbose_name=u"shengri", null=True, blank=True)
    gender = models.CharField(max_length=5, choices=(("male",u"nan"),("female",u"nv")), default="female")
    address = models.CharField(max_length=100, default=u"unknow")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"yonghuxinxi"
        verbose_name_plural = verbose_name


    # 设定返回的信息
    def __unicode__(self):
        return self.username

