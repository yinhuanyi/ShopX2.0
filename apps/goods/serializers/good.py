# coding: utf-8
"""
@Author: Robby
@Module name: good.py
@Create date: 2019-09-27
@Function: 
"""
from rest_framework import serializers
from ..models.good import Goods

class GoodsSerializer(serializers.ModelSerializer):
    '''
    商品序列化
    '''

    class Meta:
        model = Goods
        fields = "__all__"