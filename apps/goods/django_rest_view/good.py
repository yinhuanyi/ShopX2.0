# coding: utf-8
"""
@Author: Robby
@Module name: goods.py
@Create date: 2019-09-27
@Function: 
"""
from rest_framework import mixins,viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models.good import Goods
from ..models import Goods
from ..serializers.good import GoodsSerializer
from ..filters.good import GoodsFilter

# 商品分页
class StandardResultsSetPagination(PageNumberPagination):
    page_query_param = 'current_page'
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 6
    ordering = 'id'

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    # 这里需要重新将queryset赋值
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    # 指定使用的过滤类
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # 指定需要过滤的类
    filter_class = GoodsFilter
    # 基于drf的filter，指定需要搜索的字典，
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 指定排序的字段
    ordering_fields = ('shop_price',)

    # 重写get_queryset方法，实现对数据过滤
    def get_queryset(self):
        queryset = Goods.objects.all()
        price_min = self.request.query_params.get("price_min", 0)
        if price_min:
            queryset = queryset.filter(shop_price__gt=int(price_min))
        return queryset