# coding: utf-8
"""
@Author: Robby
@Module name: goods.py
@Create date: 2019-09-27
@Function: 
"""
from django_filters import rest_framework as filters, NumberFilter, CharFilter
from ..models.good import Goods
from django.db.models import Q

class GoodsFilter(filters.FilterSet):
    # 初始化过滤对象，对goods的价格小于等于或大于等于过滤
    pricemin = NumberFilter(field_name='shop_price', lookup_expr='gte')
    pricemax = NumberFilter(field_name='shop_price', lookup_expr='lte')
    # SQL的搜索过滤
    name = CharFilter(field_name='name', lookup_expr='icontains')

    # 根据一级类别的id过滤出属于一级类别的所有的商品
    top_category = NumberFilter(method='top_catetory_filter')

    def top_catetory_filter(self, queryset, name, value):
        # 这里的queryset返回的是Goods的实例列表，过滤商品类别等于value的实例或者商品类别的父类别等于value的实例或者商品类别的爷爷类别等于value的实例
        # 这里category、parent_category都是外键，那么要获取外键的ID，直接在后面加上_id即可获取
        # 这里主要逻辑的实现是基于Goods这个Model有一个外键category属于GoodCategory这个Model, 这样就可以使用获取一个商品后，找到其一级类别，最后根据过滤规则判断是否这个一级类别的值等于value， 如果等于，那么这个商品将会保留下来
        queryset = queryset.filter(Q(category_id = value) | \
                                   Q(category__parent_category_id = value) | \
                                   Q(category__parent_category__parent_category_id = value))
        return queryset


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name', 'is_hot', 'is_new']



