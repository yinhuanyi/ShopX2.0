# coding: utf-8
"""
@Author: Robby
@Module name: verify_code.py
@Create date: 2019-09-29
@Function: 
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
import re
from Mxshop.settings import REGEX_MOBILE
from datetime import datetime, timedelta
from ..models import VerifyCode


User = get_user_model()

class MsmSerializer(serializers.Serializer):

    # 指定对mobile字段序列化
    mobile = serializers.CharField(max_length=11)


    # 对post请求提交的mobile字段验证其合法性
    def validate_mobile(self, mobile):
        # 查询用户这个表是否已经有电话号码注册了, 这个.count()是获得queryset中元素的个数
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 限制验证码发送频率
        one_minute_ago = datetime.now() - timedelta(hours=0, minutes=0, seconds=60)
        #
        if VerifyCode.objects.filter(add_time__gt=one_minute_ago, mobile=mobile):
            raise serializers.ValidationError("请在60后再请求验证码")

        return mobile


