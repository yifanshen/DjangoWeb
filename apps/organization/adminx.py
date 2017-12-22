# -*- coding: utf-8 -*-
__author__ = 'Evan'
__date__ = '17/12/2017 1:42 PM'

import xadmin

from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin(object):

    # 在后台展示的时候的表格形式
    list_display = ['name', 'desc', 'add_time']
    # 添加一个搜索按钮，搜索的区域如下
    search_fields = ['name', 'desc']
    # 添加一个过滤按钮，搜索的区域如下 course__name 表示取得course 这个外键的name属性
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):


    # 在后台展示的时候的表格形式
    list_display = ['name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'city', 'add_time']
    # 添加一个搜索按钮，搜索的区域如下
    search_fields = ['name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'city']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter = ['name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'city', 'add_time']


class TeacherAdmin(object):


    # 在后台展示的时候的表格形式
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_num']
    # 添加一个搜索按钮，搜索的区域如下
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_num']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)