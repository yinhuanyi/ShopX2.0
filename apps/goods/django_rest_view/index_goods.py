# coding: utf-8
"""
@Author: Robby
@Module name: index_goods.py
@Create date: 2019-10-03
@Function: 
"""
from rest_framework import mixins, viewsets
from ..models import GoodsCategory
from ..serializers import IndexCategorySerializer

# 提供查询接口
class IndexCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=['生鲜食品', '酒水饮料'])
    serializer_class = IndexCategorySerializer