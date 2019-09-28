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
from goods.django_rest_view.good import GoodsListViewSet
from goods.django_rest_view.category import CategoryViewSet
# rest framework
from rest_framework.documentation import include_docs_urls


# 导入默认路由
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# 配置将访问goods的url让GoodsListViewSet这个view处理
router.register(r'goods', GoodsListViewSet, base_name='goods')
router.register(r'categorys', CategoryViewSet, base_name='categorys')


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # rest url
    url(r'docs/',  include_docs_urls(title='电商平台')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^goods/$', goods_list, name='goods'),
    url(r'^', include(router.urls)),

]


















