# coding: utf-8
"""
@Author: Robby
@Module name: user_order.py
@Create date: 2019-10-01
@Function: 
"""
import time
from random import Random
from rest_framework import serializers
from ..models import OrderInfo, OrderGoods
from goods.serializers import GoodsSerializer


# 从表
class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)
    class Meta:
        model = OrderGoods
        fields = '__all__'

# 主表
class UserOrderDetailSerializer(serializers.ModelSerializer):
    # 这个goods是related_name，
    goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'

class UserOrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    add_time = serializers.DateTimeField(read_only=True)

    # 生成订单号
    @property
    def generate_order_sn(self):
        # 当前时间 + userid + 随机数
        return '{timestamp}{userid}{randnum}'.format(timestamp = time.strftime('%Y%m%d%H%M%S'), userid=self.context['request'].user, randnum=Random().randint(10,99))

    # 当CreateModelMixin中create方法执行self.perform_create(serializer)之前会调用validate方法
    def validate(self, attrs):
        attrs['order_sn'] = self.generate_order_sn
        return attrs

    class Meta:
        model = OrderInfo
        fields = '__all__'