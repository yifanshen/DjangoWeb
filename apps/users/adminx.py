# -*- coding: utf-8 -*-
__author__ = 'Evan'
__date__ = '17/12/2017 12:39 PM'


import  xadmin
from xadmin import views

from .models import EmailVerifyRecord
from .models import Banne

#5-5 ->|
#设置主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

#设置全局变量
class GlobalSettings(object):
    site_title = "Yifan's Admin"
    site_footer = "Yifan's Company"
    #把menu收起来
    menu_style = "accordion"


# 5-3 ->|

class EmailVerifyRecordAdmin(object):
    #在后台展示的时候的表格形式
    list_display = ['code', 'email','send_type', 'send_time']
    #添加一个搜索按钮，搜索的区域如下
    search_fields = ['code', 'email', 'send_type']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter =['code', 'email','send_type', 'send_time']


class BanneAdmin(object):


    #在后台展示的时候的表格形式
    list_display = ['titile', 'image','url', 'index','add_time']
    #添加一个搜索按钮，搜索的区域如下
    search_fields = ['titile', 'image','url', 'index']
    # 添加一个过滤按钮，搜索的区域如下
    list_filter =['titile', 'image','url', 'index','add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banne, BanneAdmin)
#设置主题功能
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
