# coding: utf-8
"""
@Author: Robby
@Module name: user_fav.py
@Create date: 2019-09-30
@Function: 
"""
from rest_framework import mixins, viewsets
from ..serializers import UserFavSerializer
from ..models import UserFav
from rest_framework.permissions import  IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
# 使得用户删除数据的时候必须使用JWT认证
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# 使得获取list列表页可以基于session认证
from rest_framework.authentication import SessionAuthentication
from ..serializers import UserFavDetailSerializer

# 收藏就是创建记录，取消收藏就是删除记录
class UserFavViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer
    # 让这个UserFavViewSet必须是登录用户才能访问
    # 有了IsOwnerOrReadOnly，当用户删除的时候，就会获取其权限
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # 局部使用JWT的token认证，不用在全局都是用token认证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 指定RetrieveModelMixin查询的是goods_id字段
    lookup_field = 'goods_id'

    # 当用户获取list列表的时候，不应该获取所有的数据，只能获取自己收藏的数据，因此需要重写get_queryset方法
    def get_queryset(self):
        queryset = UserFav.objects.filter(user=self.request.user)
        return queryset

    # 根据用户的操作选择不同的序列化类
    def get_serializer_class(self):
        return UserFavDetailSerializer if self.action == 'list' else UserFavSerializer

    # # 当用户点击某个商品收藏，发送post请求的时候，让这个商品的fav_num加1
    # def perform_create(self, serializer):
    #     # 这个instance是UserFav这个Model，Model有一个外键为goods
    #     instance = serializer.save()
    #     goods = instance.goods
    #     goods.fav_num += 1
    #     goods.save()

