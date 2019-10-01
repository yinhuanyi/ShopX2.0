# coding: utf-8
"""
@Author: Robby
@Module name: verify_code.py
@Create date: 2019-09-29
@Function: 
"""
from rest_framework import mixins
from rest_framework import viewsets
from ..serializers import MsmSerializer
from rest_framework.response import Response
from rest_framework import status
from utils.msg_code import WYMSM
from random import choice
from ..models import VerifyCode

# 接收post请求
class SMSVerifyCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = MsmSerializer

    # 生成4位数的验证码
    def generate_code(self):
        sends = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(sends))
        return ''.join(random_str)

    # 重写create方法
    def create(self, request, *args, **kwargs):
        # 获取到post提交mobile的结果
        serializer = self.get_serializer(data=request.data)

        # 判断mobile是否合法，如果合法继续执行下面的操作，不合法直接Response 400错误
        serializer.is_valid(raise_exception=True)

        # 如果mobile合法，获取用户提交的mobile
        mobile = serializer.validated_data['mobile']


        # 发送网易验证码到用户
        wy = WYMSM(mobile, self.generate_code())
        ret = wy.send()
        # 这是网易云生成的随机验证码
        real_code = ret['obj']
        # 网易云状态码
        code = ret['code']

        # 判断，如果短信发送失败返回400
        if code != 200:
            return Response(data={'mobile': mobile}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 如果发送成功，返回201, 且写入数据表
            verify_code = VerifyCode(code=real_code, mobile=mobile)
            verify_code.save()
            return Response(data={'mobile': mobile}, status=status.HTTP_201_CREATED)
