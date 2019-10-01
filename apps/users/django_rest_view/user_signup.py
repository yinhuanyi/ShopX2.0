# coding: utf-8
"""
@Author: Robby
@Module name: user_login.py
@Create date: 2019-09-29
@Function: 
"""
from rest_framework import mixins, viewsets
from ..serializers import UserRegSerializer, UserDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

User = get_user_model()

# 这里是CreateModelMixin，表示只处理post请求
#
class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    # 默认的序列化类
    serializer_class = UserRegSerializer

    # 这里是保证用户在登录的情况下才能访问这个接口
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication, )
    # authentication_classes = (SessionAuthentication, )

    # 如果用户注册完毕之后，让用户直接登录了，那么就需要将JWT的token返回给用户
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # 返回请求的时候，将用户的token也返回
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['name'] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    # 重写get_object方法，返回当前用户的数据库记录
    def get_object(self):
        return self.request.user

    # # 重写get_permissions方法，明确指明如果是retrive，用户才需要处于登录状态，其他情况不需要
    # # 目的是客户端请求用户详情数据时候，需要在登录状态
    def get_permissions(self):
        return [permissions.IsAuthenticated()] if self.action == 'retrieve' else []

    # # 重写genericAPIView中的get_serializer_class方法，明确指定如果是用户的详细信息使用UserDetailSerializer, 其他情况使用UserRegSerializer
    # # 目的是客户端请求用户详情页的时候，返回需要的字段
    def get_serializer_class(self):
        return UserDetailSerializer if self.action == 'retrieve' or self.action == 'partial_update' else UserRegSerializer


















