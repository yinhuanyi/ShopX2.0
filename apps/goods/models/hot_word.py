# coding: utf-8
"""
@Author: Robby
@Module name: hot_words.py
@Create date: 2019-09-27
@Function: 
"""
from datetime import datetime
from django.db import models


# 设置用户热搜
class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords