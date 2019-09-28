# coding: utf-8
"""
@Author: Robby
@Module name: category.py
@Create date: 2019-09-27
@Function: 
"""
from rest_framework import mixins,viewsets
from ..models.category import GoodsCategory
from ..serializers.category import GoodsCategorySerializer1


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    list:
        商品分类类别数据
    '''

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer1

