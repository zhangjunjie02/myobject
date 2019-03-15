#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url
from web.views import index

urlpatterns = [
    url(r'^$', index.index,name='index'),
]