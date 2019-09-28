# coding: utf-8
"""
@Author: Robby
@Module name: views_bask.py
@Create date: 2019-09-26
@Function: 
"""
from django.views.generic.base import View
from goods.models.good import Goods
import json
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse



class TestView(View):
    def get(self, request):
        goods = Goods.objects.all()[:10]
        # 直接将数据库中的QuerySet对象转换为json数据格式
        goods_json = serialize('json', goods)
        print(type(goods_json))
        print('serialize: --------{}'.format(goods_json))
        return HttpResponse(content=goods_json, content_type='application/json')

    def post(self,request):
        pass