# coding: utf-8
"""
@Author: Robby
@Module name: user_login.py
@Create date: 2019-09-29
@Function: 
"""
from datetime import datetime, timedelta
from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import VerifyCode
from rest_framework.validators import UniqueValidator

User = get_user_model()

class UserRegSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True,
                                     allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户已经存在')],
                                     label='用户名')

    # 这个code是一个多余的字段，不会保存到数据库中，只是做验证，因此需要在validate方法中将字段删除
    # write_only表示不需要序列化，不被API输出
    code = serializers.CharField(required=True,
                                 max_length=4,
                                 min_length=4,
                                 help_text='验证码',
                                 error_messages={'required': '请输入验证码', 'max_length': '验证码格式错误', 'min_length': '验证码格式错误', 'blank': '请输入验证码'},
                                 label='验证码',
                                 write_only=True)


    # style表示不明文显示密码，且为write_only字段表明password不需要被序列化API返回
    password = serializers.CharField(style={'input_type': 'password'},
                                     label='密码' ,
                                     write_only=True)

    # 这里的code是用户post进来的code
    def validate_code(self, code):

        # 这里是取出VerifyCode手机号等于用户post的用户名的记录，按照倒叙排序
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by("-add_time")
        # 如果用户名存在
        if verify_records:
            # 取出最后一条记录
            last_records = verify_records[0]

            # 验证验证码时间过期
            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_minutes_ago > last_records.add_time:
                raise serializers.ValidationError('验证码过期')
            # 验证验证码准确性
            if last_records.code != code:
                raise serializers.ValidationError('验证码过期')
        # 如果用户名不存在
        else:
            raise serializers.ValidationError('验证码或电话号码错误')

    # 对最后的合法字段进行过滤
    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    # 由于ModelSerializer保存字段的时候是明文，密码需要加密保存
    def create(self, validated_data):
        # 先调用父类的create方法，获取user这一条记录对象
        user = super().create(validated_data=validated_data)
        # 让密码加密
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        # 这里由于对User这个model中的mobile字段设置的是可以为空，如果用户登录的时候，没有post mobile字段，那么不会报错
        fields = ('username', 'code', 'mobile', 'password')


