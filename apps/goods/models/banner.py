# coding: utf-8
"""
@Author: Robby
@Module name: banner.py
@Create date: 2019-09-27
@Function: 
"""
from datetime import datetime
from django.db import models
from .good import Goods

# 设置轮播的商品
class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品")
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name