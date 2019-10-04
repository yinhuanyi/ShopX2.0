# coding: utf-8
"""
@Author: Robby
@Module name: signals.py
@Create date: 2019-09-29
@Function: 
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import UserFav

# 指定接收UserFav这个Model的post_save信号量
@receiver(post_save, sender=UserFav)
def create_userfav(sender, instance=None, created=False, **kwargs):
    if created:
        goods = instance.goods
        goods.fav_num += 1
        goods.save()


@receiver(post_delete, sender=UserFav)
def delete_userfav(sender, instance=None, created=False, **kwargs):
    goods = instance.goods
    goods.fav_num -= 1
    goods.save()