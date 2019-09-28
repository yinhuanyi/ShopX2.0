# coding: utf-8
"""
@Author: Robby
@Module name: category.py
@Create date: 2019-09-27
@Function: 
"""
from rest_framework import serializers
from ..models.category import GoodsCategory

class GoodsCategorySerializer3(serializers.ModelSerializer):
    '''
    商品三级类别序列化，代表：羊肉
    '''

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer2(serializers.ModelSerializer):
    '''
    商品二级类别序列化，代表：精品肉类
    '''
    sub_cat = GoodsCategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer1(serializers.ModelSerializer):
    '''
    商品一级类别序列化, 代表：生鲜食品
    '''
    # 这里一定要注意，因为一级类别低下有多个二级类别，因此many=True必须加上
    sub_cat = GoodsCategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"
