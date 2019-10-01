# coding: utf-8
"""
@Author: Robby
@Module name: good.py
@Create date: 2019-09-27
@Function: 
"""
from rest_framework import serializers
from ..models import Goods, GoodsImage

# GoodsImage作为GoodsSerializer子serializers
class GoodsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsImage
        fields = ('image', )

class GoodsSerializer(serializers.ModelSerializer):
    '''
    商品序列化
    '''
    # images_to_goods需要与GoodsImage这个Model中的goods外键的related_name的名称一致, 因为有多张图片，所以设置many=True
    images_to_goods = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"