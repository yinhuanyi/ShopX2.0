# coding: utf-8
"""
@Author: Robby
@Module name: order.py
@Create date: 2019-10-01
@Function: 
"""
from rest_framework import mixins, viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from ..models import ShoppingCart
from ..serializers import UserOrderSerializer, UserOrderDetailSerializer
from ..models import OrderInfo, OrderGoods


class UserOrderViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):

    queryset = OrderInfo.objects.all()
    serializer_class = UserOrderSerializer
    # 有了IsOwnerOrReadOnly，当用户删除的时候，就会获取其权限
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # 局部使用JWT的token认证，不用在全局都是用token认证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)

    # 用户post提交请求的时候，需要创建订单, 同时清空购物车
    def perform_create(self, serializer):

        # 生成订单，将订单信息写入数据表
        order = serializer.save()

        # 获取当前用户的购物车记录，将记录添加到OrderGoods数据表中
        shopcart_records = ShoppingCart.objects.filter(user=self.request.user)
        for shopcart_record in shopcart_records:
            # 创建订单商品数据模型，写入数据库
            order_goods_record = OrderGoods()
            order_goods_record.goods = shopcart_record.goods
            order_goods_record.goods_num = shopcart_record.nums
            order_goods_record.order = order
            order_goods_record.save()

            # 删除购物车的记录
            shopcart_record.delete()

    def get_serializer_class(self):
        return UserOrderDetailSerializer if self.action == 'retrieve' else UserOrderSerializer




