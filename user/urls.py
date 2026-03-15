# -*- coding: utf-8 -*-
"""
@Time    : 2026/3/13 14:14
@Author  : kaede
@Email   : flowerslanguage@126.com
@File    : urls.py
@Description: 文件功能描述
"""
from django.urls import path

from user.views import TestView, JwtTestView, LoginView, SaveView, PwdView, ImageView, AvatarView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('test', TestView.as_view(), name='test'),
    path('jwt_test', JwtTestView.as_view(), name='jwt_test'),
    path('save', SaveView.as_view(), name='save'),
    path('updateUserPwd', PwdView.as_view(), name='updateUserPwd'),  # 修改密码
    path('uploadImage', ImageView.as_view(), name='uploadImage'),  # 头像上传
    path('updateAvatar', AvatarView.as_view(), name='updateAvatar'),  # 更新头像

]

