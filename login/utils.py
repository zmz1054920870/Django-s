#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : utils.py
import re
from login.models import User


def check_username(username):
    content = {
        'code': 200,
        'prompt': 'successful'
    }
    if User.objects.filter(name=username):
        content['code'] = 400
        content['prompt'] = '账号已注册'
        return content
    return content


def check_phone(phone_number):
    content = {
        'code': 200,
        'prompt': 'successful'
    }
    pattern = r"^1([35789]\d|47)\d{8}$"
    if not re.match(pattern, phone_number):
        content['code'] = 400
        content['prompt'] = '手机号码格式不正确'
        return content
    if not phone_number:
        content['code'] = 400
        content['prompt'] = '手机号码为空'
        return content
    if len(phone_number) != 11:
        content['code'] = 400
        content['prompt'] = '手机号码长度不合规'
        return content
    return content


def check_password(password, confirm_password):
    content = {
        'code': 200,
        'prompt': 'successful'
    }
    pattern = r'^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$'
    if not password:
        content['code'] = 400
        content['prompt'] = '密码不能为空'
        return content
    if not re.search(pattern, password):
        content['code'] = 400
        content['prompt'] = '密码必须为6-16位字母数字的混合'
        return content
    if not confirm_password:
        content['code'] = 400
        content['prompt'] = '确认密码不能为空'
        return content
    if password != confirm_password:
        content['code'] = 400
        content['prompt'] = '两次密码不一致'
        return content
    return content


def verify_login(username, password):
    content = {
        'code': 200,
        'prompt': 'successful'
    }
    all_user = User.objects.filter(name=username)
    if not all_user:
        content['code'] = 400
        content['prompt'] = '账号不存在'
        return content
    for item in all_user:
        if item.pwd != password:
            content['code'] = 400
            content['prompt'] = '密码错误'
            return content
    return content
