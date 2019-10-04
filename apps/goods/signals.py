# coding: utf-8
"""
@Author: Robby
@Module name: signals.py
@Create date: 2019-09-29
@Function: 
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from goods.models import Goods

# 指定接收Goods这个Model的信号量, 这里接收的信号量是post_save，其实还有很多信号量
@receiver(post_save, sender=Goods)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        pass