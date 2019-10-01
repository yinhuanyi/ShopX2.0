# coding: utf-8
"""
@Author: Robby
@Module name: user_address.py
@Create date: 2019-10-01
@Function: 
"""
from rest_framework import serializers
from ..models import UserAddress

class UserAddressSerializer(serializers.ModelSerializer):
    # user字段不返回，也不能post数据，因此使用HiddenField
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # add_time字段设置read_only=True，明确指定字段不写入数据表，只返回客户端
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = UserAddress
        fields = ('id','user', 'province', 'city', 'district', 'address','signer_name', 'signer_mobile', 'add_time')