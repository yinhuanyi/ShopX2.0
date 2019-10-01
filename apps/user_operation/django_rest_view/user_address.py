# coding: utf-8
"""
@Author: Robby
@Module name: user_address.py
@Create date: 2019-10-01
@Function: 
"""
from rest_framework import  viewsets
from ..models import UserAddress
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from ..serializers import UserAddressSerializer

# 这里继承ModelViewSet是因为这个接口有create, list, update, destroy操作，那么直接继承ModelViewSet就都有了
class UserAddressViewSet(viewsets.ModelViewSet):

    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    # 有了IsOwnerOrReadOnly，当用户删除的时候，就会获取其权限
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # 局部使用JWT的token认证，不用在全局都是用token认证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)


    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)

