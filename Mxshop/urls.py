"""Mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import xadmin
from Mxshop.settings import MEDIA_ROOT
from django.views.static import serve
from goods.django_rest_view import GoodsListViewSet, CategoryViewSet, BannerViewSet, IndexCategoryViewSet
from users.django_rest_view import SMSVerifyCodeViewSet, UserViewSet
from user_operation.django_rest_view import UserFavViewSet, UserLivingMessageViewSet, UserAddressViewSet
from trade.django_rest_view import ShoppingCartViewSet, UserOrderViewSet


# rest framework
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from trade.django_rest_view import AliPayView


# 导入默认路由
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# 配置将访问goods的url让GoodsListViewSet这个view处理
router.register(r'goods', GoodsListViewSet, base_name='goods')
# 类别列表功能
router.register(r'categorys', CategoryViewSet, base_name='categorys')
# 用户注册发送短信验证码的路由
router.register(r'codes', SMSVerifyCodeViewSet, base_name='codes')
# 用户注册功能
router.register(r'users', UserViewSet, base_name='users')
# 用户收藏功能
router.register(r'userfavs', UserFavViewSet, base_name='userfavs')
# 用户留言信息
router.register(r'messages', UserLivingMessageViewSet, base_name='messages')
# 用户后货地址
router.register(r'address', UserAddressViewSet, base_name='address')
# 购物车功能
router.register(r'shopcarts', ShoppingCartViewSet, base_name='shopcarts')
# 用户订单功能
router.register(r'orders', UserOrderViewSet, base_name='orders')
# 轮播图展示
router.register(r'banners', BannerViewSet, base_name='banners')
# 首页类别查询
router.register(r'index_category_goods', IndexCategoryViewSet, base_name='index_category_goods')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # DRF文档接口
    url(r'docs/',  include_docs_urls(title='电商平台')),
    # DRF认证接口
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 全局路由
    url(r'^', include(router.urls)),
    # 配置第三方的jwt
    url(r'^login/', obtain_jwt_token),

    url(r'alipay/return', AliPayView.as_view(), name='alipay')
]


















