# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"chengshi")
    desc = models.CharField(max_length=200, verbose_name=u"miaoshu")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"chengshi"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"jigoumingchen")
    desc = models.TextField(verbose_name=u"jigoumiaoshu")
    click_num = models.IntegerField(default=0, verbose_name=u"dianjishu")
    fav_num = models.IntegerField(default=0, verbose_name=u"shoucangrenshu")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"fengmiantu", max_length=100)
    address = models.CharField(max_length=150, verbose_name=u"jigoudizhi")
    city = models.ForeignKey(CityDict, verbose_name=u"suozaichengshi")
    add_time = models.DateTimeField(default=datetime.now)


    class Meta:
        verbose_name = u"kechengjigou"
        verbose_name_plural = verbose_name



class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"suoshujigou")
    name = models.CharField(max_length=50, verbose_name=u"jiaoshiming")
    work_years = models.IntegerField(default=0, verbose_name=u"gongzuonianxian")
    work_company = models.CharField(max_length=50, verbose_name=u"jiuzhigongsi")
    work_position = models.CharField(max_length=50, verbose_name=u"gongsizhiwei")
    points = models.CharField(max_length=50, verbose_name=u"jiaoxuetedian")
    click_num = models.IntegerField(default=0, verbose_name=u"dianjishu")
    fav_num = models.IntegerField(default=0, verbose_name=u"shoucangrenshu")

    class Meta:
        verbose_name = u"jiaoshi"
        verbose_name_plural = verbose_name