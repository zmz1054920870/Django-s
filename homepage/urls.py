#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : urls.py
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'page/1', page_one, name='one'),
    path(r'page/2', page_two, name='two'),
    path(r'page/3', page_three, name='three'),
    path(r'page/4', page_four, name='four'),
    path(r'page/5', page_two),
]