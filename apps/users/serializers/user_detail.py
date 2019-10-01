# coding: utf-8
"""
@Author: Robby
@Module name: user_detail.py
@Create date: 2019-09-30
@Function: 
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# 返回用户详情的序列化字段
class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'gender', 'birthday', 'email', 'mobile')

