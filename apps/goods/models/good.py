# coding: utf-8
"""
@Author: Robby
@Module name: goods.py
@Create date: 2019-09-27
@Function: 
"""
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField
from .category import GoodsCategory
# 商品的model
class Goods(models.Model):
    """
    商品
    """
    # 商品属于哪个类别， 子model是商品，父model是类别
    category = models.ForeignKey(GoodsCategory, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    # 这里是用的是第三方的extra_apps
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300, filePath="goods/files/", default='')
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    # 图片将会上传到media/goods/images/目录下
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name