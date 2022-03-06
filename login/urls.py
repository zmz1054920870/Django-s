#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : urls.py
from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('login/', login),
    path('login_out/', login_out),
    path('register/', register),
    path('index/', index),
    re_path(r'test/(?P<id>\d+)/(?P<name>\w+)/', test),
    # path('index/', )
]