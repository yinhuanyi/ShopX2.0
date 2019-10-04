# coding: utf-8
"""
@Author: Robby
@Module name: banner.py
@Create date: 2019-10-03
@Function: 
"""
from rest_framework import mixins, viewsets
from ..models import Banner
from ..serializers import BannerSerializer

class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerializer