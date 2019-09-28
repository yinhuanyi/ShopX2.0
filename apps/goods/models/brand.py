# coding: utf-8
"""
@Author: Robby
@Module name: brand.py
@Create date: 2019-09-27
@Function: 
"""
from datetime import datetime
from django.db import models
from .category import GoodsCategory

# 定义商品的品牌
class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    # 这里是指定哪个品牌属于哪个类别，因此品牌是子model，类别是父model
    category = models.ForeignKey(GoodsCategory, related_name='brands_to_category', null=True, blank=True, verbose_name="商品类目")
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")
    # 图片上传会上传到medis/brands目录下, brands目录会自动生成，无需新建
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand"

    def __str__(self):
        return self.name