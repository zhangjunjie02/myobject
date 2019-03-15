#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

import re
class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        urllist = ['/myadmin/login', '/myadmin/dologin', '/myadmin/logout','/myadmin/verify']
        # 获取当前请求路径
        path = request.path
        # print("Hello World!"+path)
        # 判断当前请求是否是访问网站后台,并且path不在urllist中
        if re.match("/myadmin", path) and (path not in urllist):
            # 判断当前用户是否没有登录
            if "adminuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('myadmin_login'))


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response