#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url
from myadmin.views import index,users,types,goods


urlpatterns = [
    #后台首页
    url(r'^$', index.index,name='myadmin_index'),
    #后台管理路由
    url(r'^login$', index.login, name="myadmin_login"),
    url(r'^dologin$', index.dologin, name="myadmin_dologin"),
    url(r'^logout$', index.logout, name="myadmin_logout"),
    #验证码的路由
    url(r'^verify$', index.verify, name="myadmin_verify"),  # 验证码
    #会员信息管理路由

    url(r'^users$', users.index,name='myadmin_users_index'),
    url(r'^users/resetpd$', users.resetpassword,name='myadmin_users_resetpd'),
    url(r'^users/add$', users.add,name='myadmin_users_add'),
    url(r'^users/insert$', users.insert,name='myadmin_users_insert'),
    url(r'^users/del/(?P<uid>[0-9]+)$', users.delete,name='myadmin_users_del'),
    url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit,name='myadmin_users_edit'),
    url(r'^users/update/(?P<uid>[0-9]+)$', users.update,name='myadmin_users_update'),



    #商品类别管理路由
    url(r'^type$', types.index, name='myadmin_types_index'),
    url(r'^type/add/(?P<tid>[0-9]+)$', types.add, name='myadmin_types_add'),
    url(r'^type/insert$', types.insert, name='myadmin_types_insert'),
    url(r'^type/del/(?P<tid>[0-9]+)$', types.delete, name='myadmin_types_del'),
    url(r'^type/edit/(?P<tid>[0-9]+)$', types.edit, name='myadmin_types_edit'),
    url(r'^type/update/(?P<tid>[0-9]+)$', types.update, name='myadmin_types_update'),



    #商品信息路由

    url(r'^goods/(?P<pIndex>[0-9]+)$', goods.index, name='myadmin_goods_index'),
    url(r'^goods/add$', goods.add, name='myadmin_goods_add'),
    url(r'^goods/insert$', goods.insert, name='myadmin_goods_insert'),
    url(r'^goods/del/(?P<gid>[0-9]+)$', goods.delete, name='myadmin_goods_del'),
    url(r'^goods/edit/(?P<gid>[0-9]+)$', goods.edit, name='myadmin_goods_edit'),
    url(r'^goods/update/(?P<gid>[0-9]+)$', goods.update, name='myadmin_goods_update'),





]