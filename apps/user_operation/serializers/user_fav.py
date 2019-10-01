# coding: utf-8
"""
@Author: Robby
@Module name: user_fav.py
@Create date: 2019-09-30
@Function: 
"""
from rest_framework import serializers
from ..models import UserFav
from rest_framework.validators import UniqueTogetherValidator
from goods.serializers import GoodsSerializer


class UserFavDetailSerializer(serializers.ModelSerializer):

    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        # 对一个Model实例需要有删除功能，就需要将id返回
        fields = ('goods', 'id')


class UserFavSerializer(serializers.ModelSerializer):
    # 因为这个user和goods都是外键，导致用户post只能选择数据进行post，因此这里的用户post应该是获取当前的用户
    # HiddenField是不会被序列化返回的
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        # 对一个Model实例需要有删除功能，就需要将id返回
        fields = ('user', 'goods', 'id')

        # 设置联合唯一字段, 让'user', 'goods'成为联合唯一，这是对数据库的操作，设置完毕后一定需要migration
        unique_together = ('user', 'goods')

        # 也可以使用rest_framework中的联合唯一索引
        validators = [
            UniqueTogetherValidator(queryset=UserFav.objects.all(), fields=('user', 'goods'), message='已经收藏过')
        ]

