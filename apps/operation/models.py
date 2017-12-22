# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import  datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course

# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"xingming")
    mobile = models.CharField(max_length=11, verbose_name=u"shouji")
    course_name = models.CharField(max_length=50, verbose_name=u"kechengming")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"tianjiashijian")

    class Meta:
        verbose_name = u"yonghuzixun"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    "课程评论"
    user = models.ForeignKey(UserProfile, verbose_name=u"yonghuming")
    course = models.ForeignKey(Course, verbose_name=u"kecheng")
    comments = models.CharField(max_length=200, verbose_name=u"pinglun")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"tianjiashijian")

    class Meta:
        verbose_name = u"kechengpinglun"

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"yonghuming")
    fav_id = models.IntegerField(default=0, verbose_name=u"shujuid")
    fav_type = models.IntegerField(choices=((1,"kecheng"),(2,"kechengjigou"),(3,"jiangshi")),default=1, verbose_name="shoucangleixing")

    class Meta:
        verbose_name=u"yonghushoucang"
        verbose_name_plural = verbose_name

class UserMesaage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"jieshouyonghu")
    message = models.CharField(max_length=500, verbose_name=u"xiaoxineirong")
    has_read = models.BooleanField(default= False, verbose_name=u"shifouyidu")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"tianjiashijian")

    class Meta:
        verbose_name=u"yonghuxiaoxi"
        verbose_name_plural = verbose_name

class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"yonghuming")
    course = models.ForeignKey(Course, verbose_name=u"kecheng")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"tianjiashijian")

    class Meta:
        verbose_name=u"yonghukecheng"
        verbose_name_plural = verbose_name