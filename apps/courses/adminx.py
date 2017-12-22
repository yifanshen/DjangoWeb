# -*- coding: utf-8 -*-
__author__ = 'Evan'
__date__ = '17/12/2017 1:25 PM'

from .models import Course, Lesson, Video, CourseResource
import  xadmin

class CourseAdmin(object):


    #在后台展示的时候的表格形式
    list_display = ['name', 'desc','detail', 'degree','learn_times', 'students', 'fav_num', 'image', 'click_num','add_time']
    #添加一个搜索按钮，搜索的区域如下
    search_fields = ['name', 'desc','detail', 'degree','learn_times', 'students', 'fav_num', 'image', 'click_num']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter =['name', 'desc','detail', 'degree','learn_times', 'students', 'fav_num', 'image', 'click_num','add_time']

class LessonAdmin(object):


    #在后台展示的时候的表格形式
    list_display = ['course', 'name', 'add_time']
    #添加一个搜索按钮，搜索的区域如下
    search_fields = ['course', 'name']
    # 添加一个过滤按钮，搜索的区域如下 course__name 表示取得course 这个外键的name属性
    list_filter =['course__name', 'name', 'add_time']


class VideoAdmin(object):
    # 在后台展示的时候的表格形式
    list_display = ['lesson', 'name', 'add_time']
    # 添加一个搜索按钮，搜索的区域如下
    search_fields = ['lesson', 'name']
    # 添加一个过滤按钮，搜索的区域如下 course__name 表示取得course 这个外键的name属性
    list_filter = ['lesson', 'name', 'add_time']

class CourseResourceAdmin(object):

    #在后台展示的时候的表格形式
    list_display = ['course', 'name', 'download','add_time']
    #添加一个搜索按钮，搜索的区域如下
    search_fields = ['course', 'name', 'download']
    # 添加一个过滤按钮，搜索的区域如下 course__name 表示取得course 这个外键的name属性
    list_filter =['course', 'name', 'download','add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)