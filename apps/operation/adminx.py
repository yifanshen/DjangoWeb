# -*- coding: utf-8 -*-
__author__ = 'Evan'
__date__ = '17/12/2017 1:58 PM'

import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMesaage, UserCourse

class UserAskAdmin(object):
    #在后台展示的时候的表格形式
    list_display = ['name', 'mobile','course_name', 'add_time']
    #添加一个搜索按钮，搜索的区域如下
    search_fields = ['name', 'mobile','course_name']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter =['name', 'mobile','course_name', 'add_time']

class CourseCommentsAdmin(object):

    #在后台展示的时候的表格形式
    list_display = ['user', 'course','comments', 'add_time']
    #添加一个搜索按钮，搜索的区域如下
    search_fields =['user', 'course','comments']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter =['user', 'course','comments', 'add_time']

class UserFavoriteAdmin(object):
    # 在后台展示的时候的表格形式
    list_display = ['user', 'fav_id', 'fav_type']
    # 添加一个搜索按钮，搜索的区域如下
    search_fields = ['user', 'fav_id', 'fav_type']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter = ['user', 'fav_id', 'fav_type']

class UserMesaageAdmin(object):

    # 在后台展示的时候的表格形式
    list_display = ['user', 'message', 'has_read', 'add_time']
    # 添加一个搜索按钮，搜索的区域如下
    search_fields = ['user', 'message', 'has_read']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    #在后台展示的时候的表格形式
    list_display = ['user', 'course', 'add_time']
    #添加一个搜索按钮，搜索的区域如下
    search_fields =['user', 'course']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter =['user', 'course', 'add_time']

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMesaage, UserMesaageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
