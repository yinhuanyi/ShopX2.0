# coding: utf-8
"""
@Author: Robby
@Module name: brand.py
@Create date: 2019-10-03
@Function: 
"""
from rest_framework import serializers
from ..models import GoodsCategoryBrand

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategoryBrand
        fields = '__all__'