# coding: utf-8
"""
@Author: Robby
@Module name: ad.py
@Create date: 2019-09-27
@Function: 
"""
from datetime import datetime
from django.db import models
from .category import GoodsCategory
from .good import Goods

# 设置广告，广告属于类别也属于商品
class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='category',verbose_name="商品类目")
    goods =models.ForeignKey(Goods, related_name='goods')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '首页商品类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name