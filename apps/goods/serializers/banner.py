# coding: utf-8
"""
@Author: Robby
@Module name: banner.py
@Create date: 2019-10-03
@Function: 
"""

from rest_framework import serializers
from ..models import Banner

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

    