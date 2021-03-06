# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-17 03:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='chengshi')),
                ('desc', models.CharField(max_length=200, verbose_name='miaoshu')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'chengshi',
                'verbose_name_plural': 'chengshi',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='jigoumingchen')),
                ('desc', models.TextField(verbose_name='jigoumiaoshu')),
                ('click_num', models.IntegerField(default=0, verbose_name='dianjishu')),
                ('fav_num', models.IntegerField(default=0, verbose_name='shoucangrenshu')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='fengmiantu')),
                ('address', models.CharField(max_length=150, verbose_name='jigoudizhi')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='suozaichengshi')),
            ],
            options={
                'verbose_name': 'kechengjigou',
                'verbose_name_plural': 'kechengjigou',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='jiaoshiming')),
                ('work_years', models.IntegerField(default=0, verbose_name='gongzuonianxian')),
                ('work_company', models.CharField(max_length=50, verbose_name='jiuzhigongsi')),
                ('work_position', models.CharField(max_length=50, verbose_name='gongsizhiwei')),
                ('points', models.CharField(max_length=50, verbose_name='jiaoxuetedian')),
                ('click_num', models.IntegerField(default=0, verbose_name='dianjishu')),
                ('fav_num', models.IntegerField(default=0, verbose_name='shoucangrenshu')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='suoshujigou')),
            ],
            options={
                'verbose_name': 'jiaoshi',
                'verbose_name_plural': 'jiaoshi',
            },
        ),
    ]
