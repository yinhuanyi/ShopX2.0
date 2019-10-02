# coding: utf-8
"""
@Author: Robby
@Module name: shop_cart.py
@Create date: 2019-10-01
@Function: 
"""
from rest_framework import  viewsets
from ..models import ShoppingCart
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from ..serializers import ShoppingCartSerializer, ShoppingCartDetailSerializer

class ShoppingCartViewSet(viewsets.ModelViewSet):

    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    # 有了IsOwnerOrReadOnly，当用户删除的时候，就会获取其权限
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # 局部使用JWT的token认证，不用在全局都是用token认证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 这对于update、delete操作，对查找字段id替换为goods_id
    lookup_field = 'goods_id'

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        return ShoppingCartDetailSerializer if self.action == 'list' else ShoppingCartSerializer


