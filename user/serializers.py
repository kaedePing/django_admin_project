# -*- coding: utf-8 -*-
"""
@Time    : 2026/3/13 19:02
@Author  : kaede
@Email   : flowerslanguage@126.com
@File    : serializers.py
@Description: 文件功能描述
"""
from rest_framework import serializers
from .models  import SysUser


class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = '__all__'
