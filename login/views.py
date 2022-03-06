import re
import random
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import User, Hobby
from login.utils import check_username, check_phone, check_password, verify_login


# Create your views here.


def index(request):
    uid = request.COOKIES.get('uid')
    is_login = request.COOKIES.get('is_login')
    ctx = {
        'user': User.objects.filter(id=uid).first(),
        'is_login': is_login
    }
    captcha = random.randint(1000, 9999)
    print(captcha, 111111111111111111111111111111111111111111111111111111111)
    response = render(request, template_name='index/index.html', context=ctx)
    response.set_cookie(key='captcha', value=captcha)
    return response


def register(request):
    if request.method == 'GET':
        return render(request, template_name='register/register.html')

    else:
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_check_result = check_phone(phone_number=phone)
        password_check_result = check_password(password, confirm_password)
        username_check_result = check_username(username)
        if username_check_result['code'] == 400:
            return JsonResponse(username_check_result)
        if phone_check_result['code'] == 400:
            return JsonResponse(phone_check_result)
        if password_check_result['code'] == 400:
            return JsonResponse(password_check_result)
        user_o = User(
            phone=phone,
            name=username,
            pwd=password,
            gender=random.choice(['男', '女']),
            is_deleted=False
        )
        user_o.save()
        user_o.hb.add(1, 2)
        return render(request, template_name='login/login.html')


def login(request):
    if request.method == 'GET':
        captcha = random.randint(1000, 9999)
        print(captcha, 111111111111111111111111111111111111111111111111111111111)
        response = render(request, template_name='login/login.html')
        response.set_cookie(key='captcha', value=captcha)
        return response
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('code')
        captcha = request.COOKIES.get('captcha')
        verify_login_result = verify_login(username, password)
        if verify_login_result['code'] == 400:
            json_object = JsonResponse(verify_login_result)
            json_object.delete_cookie(key='uid')
            json_object.delete_cookie(key='is_login')
            return json_object
        if code != captcha:
            content = {
                'code': 400,
                'prompt': '验证码不对'
            }
            return JsonResponse(data=content)
        response_object = render(request, template_name='blog/blog.html')
        user_object = User.objects.filter(name=username).first()
        response_object.set_cookie(key='uid', value=user_object.id, max_age=300)
        response_object.set_cookie(key='is_login', value=1, max_age=300)
        return response_object


def login_out(request):
    response_object = render(request, template_name='index/index.html')
    response_object.delete_cookie(key='uid')
    response_object.delete_cookie(key='is_login')
    # response_object.cookies.clear()
    return response_object




def test(request, *args, **kwargs):
    print(args, 111111111111111111)
    print(kwargs, 222222222222222222222222)
    return HttpResponse(222222222222222222)



