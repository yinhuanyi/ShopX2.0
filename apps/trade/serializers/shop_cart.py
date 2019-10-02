# coding: utf-8
"""
@Author: Robby
@Module name: shop_cart.py
@Create date: 2019-10-01
@Function: 
"""
from rest_framework import serializers
from ..models import ShoppingCart
from goods.models import Goods
from goods.serializers import GoodsSerializer


# 如果是list操作使用这个serializers
class ShoppingCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()
    class Meta:
        model = ShoppingCart
        fields = '__all__'

class ShoppingCartSerializer(serializers.Serializer):

    # 首先对字段验证
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nums = serializers.IntegerField(required=True, min_value=1, error_messages={"min_value": "商品数量不能小于1", "required": "必填字段"}, label='商品数量')
    # 这个外键是直接在字段上进行扩充的，之前都创建一个新的serializers类，使用一个新字段指向这个序列化类，实现外键的信息序列化
    goods = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all(), required=True, label='商品')


    # 由于继承的是Serializer，因此需要手动重写create方法。如果是继承的ModelSerializer, 就不需要，因为在ModelSerializer中已经重写了create方法
    def create(self, validated_data):
        # 1： 先获取需要写入到数据表的数据
        # 在Serializer中的HiddenField字段是存放在self.context['request']中，如果是ModelSerializer，存放的是self.request中
        user = self.context['request'].user
        nums = validated_data['nums']
        goods = validated_data['goods']

        # 2： 查看当前user和goods的唯一索引字段是否已经存在
        queryset = ShoppingCart.objects.filter(user=user, goods=goods.id)
        # 如果存在更新记录的nums字段值,在吸入到数据表
        if queryset:
            # 必须取第一条，如果是取最后一条，会报Negative indexing is not supported
            record = queryset[0]
            record.nums += nums
            record.save()

        # 如果不存在直接写入数据表
        else:
            record = ShoppingCart.objects.create(**validated_data)
        return record


    def update(self, instance, validated_data):
        '''

        :param instance: 需要跟新的数据表模型
        :param validated_data: 验证通过的字段模型
        :return: put方法返回更新后的数据表模型
        '''
        instance.nums = validated_data['nums']
        instance.save()
        return instance








