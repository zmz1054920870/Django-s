from django.shortcuts import render, redirect, reverse
from login.views import login

# Create your views here.


def page_one(request, **kwargs):

    return redirect(to=reverse(viewname=login, urlconf='my_blog.urls', current_app='homepage'))


def page_two(request):
    return redirect(to=reverse(viewname='page:three', urlconf='my_blog.urls'))


def page_three(request):
    return render(request, template_name='homepage/page_three.html')


def page_four(request):
    return redirect(to=reverse(viewname='page:two', urlconf='my_blog.urls'))