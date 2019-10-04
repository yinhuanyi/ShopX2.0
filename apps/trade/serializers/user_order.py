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
from utils.alipay import AliPay
from Mxshop.settings import private_key_path, ali_public_key_path


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
    # 添加支付字段
    alipay_url = serializers.SerializerMethodField(read_only=True)
    # 无论是list请求还是create请求都会调用这个方法
    def get_alipay_url(self, obj):
        '''
        :param obj: 为serializer.data
        :return:
        '''
        alipay = AliPay(
            # 沙箱的appid
            appid="2016101200669671",
            # 这里一定要改为线上服务器的地址
            app_notify_url="http://线上服务器地址:8000/alipay/return",
            # 使用静态文件路径
            app_private_key_path=private_key_path,
            # 使用静态文件路径
            alipay_public_key_path=ali_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
            # debug为True，适用沙箱接口
            debug=True,  # 默认False,
            # 这里一定要改为线上服务器的地址
            return_url="http://线上服务器地址:8000/alipay/return"
        )

        url = alipay.direct_pay(
            subject=obj.order_sn,
            out_trade_no=obj.order_sn,
            total_amount=obj.order_mount
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        return re_url
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

    # 添加支付字段
    alipay_url = serializers.SerializerMethodField(read_only=True)
    # 无论是list请求还是create请求都会调用这个方法
    def get_alipay_url(self, obj):
        '''
        :param obj: 为serializer.data
        :return:
        '''
        alipay = AliPay(
            # 沙箱的appid
            appid="2016101200669671",
            # 这里一定要改为线上服务器的地址
            app_notify_url="http://线上服务器地址:8000/alipay/return",
            # 使用静态文件路径
            app_private_key_path=private_key_path,
            # 使用静态文件路径
            alipay_public_key_path=ali_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
            # debug为True，适用沙箱接口
            debug=True,  # 默认False,
            # 这里一定要改为线上服务器的地址
            return_url="http://线上服务器地址:8000/alipay/return"
        )

        url = alipay.direct_pay(
            subject=obj.order_sn,
            out_trade_no=obj.order_sn,
            total_amount=obj.order_mount
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        return re_url



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