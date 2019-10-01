# coding: utf-8
"""
@Author: Robby
@Module name: user_message.py
@Create date: 2019-10-01
@Function: 
"""
from rest_framework import mixins, viewsets
from ..serializers import UserLivingMessageSerializer
from ..models import UserLeavingMessage
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly


class UserLivingMessageViewSet(mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):

    queryset = UserLeavingMessage.objects.all()
    serializer_class = UserLivingMessageSerializer
    # 有了IsOwnerOrReadOnly，当用户删除的时候，就会获取其权限
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # 局部使用JWT的token认证，不用在全局都是用token认证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)


    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


