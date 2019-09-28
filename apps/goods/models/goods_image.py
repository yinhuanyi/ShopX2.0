# coding: utf-8
"""
@Author: Robby
@Module name: goods_image.py
@Create date: 2019-09-27
@Function: 
"""
from datetime import datetime
from django.db import models
from .good import Goods

# 商品图片
class GoodsImage(models.Model):
    """
    商品轮播图
    """
    # 图片属于商品，图片是子model，商品是父model
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images_to_goods")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name