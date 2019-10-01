# coding: utf-8
"""
@Author: Robby
@Module name: signals.py
@Create date: 2019-09-29
@Function: 
"""
# 当User这个model保存到数据库的时候，捕捉这个信号量，设置密码为密文
# 同时也需要在apps.py模块中配置

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()