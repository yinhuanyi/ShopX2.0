# coding: utf-8
"""
@Author: Robby
@Module name: index_goods.py
@Create date: 2019-10-03
@Function: 
"""
from ..models import GoodsCategory, IndexAd
from ..serializers import BrandSerializer, GoodsSerializer, GoodsCategorySerializer2
from rest_framework import serializers
from ..models import Goods
from django.db.models import Q

class IndexCategorySerializer(serializers.ModelSerializer):
    # 由于类别品牌属于类别，类别中有一个related_name=brands_to_category, 这里获取到类别之后，反向序列化获取类别品牌
    # 反向查询many=True，正向查询many=False
    brands_to_category = BrandSerializer(many=True)
    # 虽然Goods Model中有一个外键category指向GoodsCategory，好像可以反向查询，当获取到category，可以查看包含了哪些商品，但是在GoodsCategory中，类别是分多级的，因此，当获取到category的时候，可能获取的是第一类，那么第一类就没有商品，只有第三类才有商品，因此需要自己自定义的返回category下的goods信息，如果是获取的第一类的category，那么需要获取到第一类下面的所有第二类，第二类下面所有第三类，根据第三类查找所有商品
    goods = serializers.SerializerMethodField(read_only=True)
    # 获取一级分类下的二级分类
    sub_cat = GoodsCategorySerializer2(many=True)
    ad_goods = serializers.SerializerMethodField(read_only=True)

    def get_ad_goods(self, obj):
        ad_goods = IndexAd.objects.filter(category_id=obj.id)
        if ad_goods:
            good_record = ad_goods[0].goods
            return GoodsSerializer(instance=good_record, many=False, context={'request': self.context['request']}).data

    def get_goods(self, obj):
        '''
        :param obj: GoodsCategory中的记录
        :return:
        '''
        # obj.id就是类别id，如果Goods这个Model中category_id等于用户请求的类别字段，那么此商品就会保留
        all_goods_queryset = Goods.objects.filter(Q(category_id = obj.id) | \
                                         Q(category__parent_category_id = obj.id) | \
                                         Q(category__parent_category__parent_category_id = obj.id))
        # 拿到所有的记录之后需要序列化返回, GoodsSerializer中的init方法可以将需要序列化的实例传递进来，返回实例的序列化结果
        return GoodsSerializer(instance=all_goods_queryset, many=True, context={'request': self.context['request']}).data

    class Meta:
        model = GoodsCategory
        fields = '__all__'

