# coding: utf-8
"""
@Author: Robby
@Module name: goods.py
@Create date: 2019-09-27
@Function: 
"""
from django_filters import rest_framework as filters, NumberFilter, CharFilter
from ..models.good import Goods

class GoodsFilter(filters.FilterSet):
    # 初始化过滤对象，对goods的价格小于等于或大于等于过滤
    min_price = NumberFilter(field_name='shop_price', lookup_expr='gte')
    max_price = NumberFilter(field_name='shop_price', lookup_expr='lte')
    # SQL的搜索过滤
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price', 'name']