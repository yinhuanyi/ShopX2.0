# coding: utf-8
"""
@Author: Robby
@Module name: cart.py
@Create date: 2019-09-27
@Function: 
"""
from datetime import datetime
from django.db import models
# 这个是使用一种变向的方式，通过get_user_model这个函数，可以将user这个类，也就是UserProfile这个类获取到，当然也可以直接导入
from django.contrib.auth import get_user_model
from goods.models.good import Goods
# 这里拿到的其实就是也就是UserProfile这个类获取到
User = get_user_model()

# 创建购物车
class ShoppingCart(models.Model):
    """
    购物车
    """
    # 购物车是子model，User和Goods是父model
    user = models.ForeignKey(User, verbose_name=u"用户")
    goods = models.ForeignKey(Goods, verbose_name=u"商品")
    nums = models.IntegerField(default=0, verbose_name="购买数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        # 这里将用户与商品建立联合唯一索引，指明一个用户对一个商品添加记录只能有一次
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)