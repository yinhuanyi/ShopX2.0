# coding: utf-8
"""
@Author: Robby
@Module name: goods.py
@Create date: 2019-09-27
@Function: 
"""
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework import mixins,viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models import Goods
from ..serializers.good import GoodsSerializer
from ..filters.good import GoodsFilter
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# 商品分页
class StandardResultsSetPagination(PageNumberPagination):
    # 将请求参数与前端保持一致
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 12
    # 这里使用id排序会报错，所以使用售卖数排序
    ordering = 'name'


class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
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
    ordering_fields = ('sold_num','shop_price')
    throttle_classes = (UserRateThrottle, AnonRateThrottle)

    # 重写get_queryset方法，实现对数据过滤
    def get_queryset(self):
        queryset = Goods.objects.all()
        price_min = self.request.query_params.get("price_min", 0)
        if price_min:
            queryset = queryset.filter(shop_price__gt=int(price_min))
        return queryset

    # 重写retrieve方法，用户访问某个商品的时候，给商品点击数量加1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)