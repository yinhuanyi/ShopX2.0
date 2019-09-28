# coding: utf-8
"""
@Author: Robby
@Module name: fav.py
@Create date: 2019-09-27
@Function: 
"""
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from goods.models.good import Goods
User = get_user_model()

# 用户收藏
class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户")
    goods = models.ForeignKey(Goods, verbose_name="商品", help_text="商品id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username