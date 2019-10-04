# coding: utf-8
"""
@Author: Robby
@Module name: alipay.py
@Create date: 2019-10-02
@Function: 
"""
from datetime import datetime
from rest_framework.views import APIView
from utils.alipay import AliPay
from Mxshop.settings import ali_public_key_path, private_key_path
from ..models import OrderInfo
from rest_framework.response import Response


class AliPayView(APIView):
    def get(self, request):
        processed_dict = {}
        for key, value in request.GET.items():
            processed_dict[key] = value

        sign = processed_dict.pop('sign', None)

        alipay = AliPay(
            # 沙箱的appid
            appid="2016101200669671",
            # 这里一定要改为线上服务器的地址
            app_notify_url="http://线上服务器地址:8000/alipay/return",
            # 使用静态文件路径
            app_private_key_path=private_key_path,
            # 使用静态文件路径
            alipay_public_key_path=ali_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            # debug为True，适用沙箱接口
            debug=True,  # 默认False,
            # 这里一定要改为线上服务器的地址
            return_url="http://线上服务器地址:8000/alipay/return"
        )

        # 验证支付状态
        verify_result = alipay.verify(processed_dict, sign)

        # 如果支付成功，获取订单信息
        if verify_result:
            order_sn = processed_dict.get('out_trade_no', None)
            trade_no = processed_dict.get('trade_no', None)
            trade_status = processed_dict.get('trade_status', None)

            # 给订单信息的交易字段赋值，之前的交易信息为空的
            orderInfo_records = OrderInfo.objects.filter(order_sn=order_sn)
            for orderInfo_record in orderInfo_records:
                orderInfo_record.pay_status = trade_status
                orderInfo_record.trade_no = trade_no
                orderInfo_record.pay_time = datetime.now()
                orderInfo_record.save()

            # 告诉支付宝，已经收到请求且处理了
            return Response('success')

    def post(self, request):
        processed_dict = {}
        for key, value in request.POST.items():
            processed_dict[key] = value
        sign = processed_dict.pop('sign', None)

        alipay = AliPay(
            # 沙箱的appid
            appid="2016101200669671",
            # 这里一定要改为线上服务器的地址
            app_notify_url="http://线上服务器地址:8000/",
            # 使用静态文件路径
            app_private_key_path=private_key_path,
            # 使用静态文件路径
            alipay_public_key_path=ali_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            # debug为True，适用沙箱接口
            debug=True,  # 默认False,
            # 这里一定要改为线上服务器的地址
            return_url="http://线上服务器地址:8000/"
        )

        # 验证支付状态
        verify_result = alipay.verify(processed_dict, sign)

        # 如果支付成功，获取订单信息
        if verify_result:
            order_sn = processed_dict.get('out_trade_no', None)
            trade_no = processed_dict.get('trade_no', None)
            trade_status = processed_dict.get('trade_status', None)

            # 给订单信息的交易字段赋值，之前的交易信息为空的
            orderInfo_records = OrderInfo.objects.filter(order_sn=order_sn)
            for orderInfo_record in orderInfo_records:
                orderInfo_record.pay_status = trade_status
                orderInfo_record.trade_no = trade_no
                orderInfo_record.pay_time = datetime.now()
                orderInfo_record.save()

            # 告诉支付宝，已经收到请求且处理了
            return Response('success')








