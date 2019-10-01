# coding: utf-8
"""
@Author: Robby
@Module name: permissions.py
@Create date: 2019-09-30
@Function: 
"""
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # 如果不是安全的请求方法，例如delete方法，这里需要判断请求的用户是否是本条记录的用户，如果返回True才能够删除
        return obj.user == request.user