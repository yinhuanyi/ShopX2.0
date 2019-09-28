# coding: utf-8
"""
@Author: Robby
@Module name: code.py
@Create date: 2019-09-27
@Function: 
"""
from datetime import datetime
from django.db import models


# 将用户的手机验证码保存到数据库中
class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code