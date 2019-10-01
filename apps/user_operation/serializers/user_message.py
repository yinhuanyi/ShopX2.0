# coding: utf-8
"""
@Author: Robby
@Module name: user_message.py
@Create date: 2019-10-01
@Function: 
"""
from rest_framework import serializers
from ..models import UserLeavingMessage

class UserLivingMessageSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # add_time字段设置read_only=True，明确指定字段不写入数据表，只返回客户端
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = UserLeavingMessage
        fields = ('id','user', 'message_type', 'subject', 'message', 'file','add_time')