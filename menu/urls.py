# -*- coding: utf-8 -*-
"""
@Time    : 2026/3/13 14:14
@Author  : kaede
@Email   : flowerslanguage@126.com
@File    : urls.py
@Description: 文件功能描述
"""
from django.urls import path

from menu.views import TreeListView, SaveView, ActionView

urlpatterns = [
    path('treeList', TreeListView.as_view(), name='treeList'),  # 查询权限菜单树信息
    path('save', SaveView.as_view(), name='save'),  # 添加或者修改权限信息
    path('action', ActionView.as_view(), name='action'),  # 权限信息操作
]
