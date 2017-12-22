# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import  datetime

from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"kechengming")
    desc = models.CharField(max_length=300, verbose_name=u"kechengmiaoshu")
    detail = models.TextField(verbose_name=u"kechengxiangqing")
    degree = models.CharField(verbose_name=u"nandu", choices=(("cj","chuji"), ("zj", "zhongji"), ("gj","gaoji")), max_length=50)
    learn_times = models.IntegerField(default=0, verbose_name=u"xuexishichang(fenzhongshu)")
    students = models.IntegerField(default=0, verbose_name=u"xuexirenshu")
    fav_num = models.IntegerField(default=0, verbose_name=u"shoucangrenshu")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"fengmiantu", max_length=100)
    click_num = models.IntegerField(default=0, verbose_name=u"dianjishu")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"tianjiashijian")

    class Meta:
        verbose_name=u"kecheng"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"kecheng")
    name = models.CharField(max_length=100, verbose_name=u"zhangjieming")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"tianjiashijian")


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"zhangjie")
    name = models.CharField(max_length=100, verbose_name=u"shipinming")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"tianjiashijian")


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"kecheng")
    name = models.CharField(max_length=100, verbose_name=u"mingcheng")
    download = models.FileField(upload_to="course/%Y/%m", verbose_name=u"ziyuanwenjian", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"tianjiashijian")

    class Meta:
        verbose_name=u"kechengziyuan"
        verbose_name_plural = verbose_name
