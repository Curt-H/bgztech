from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from blog import validate_username, Users


def index(request):
    context_dict = {
    }
    return render(request,
                  'blog/index.html',
                  context=context_dict
                  )


def homepage(request, u=None):
    u = request.COOKIES.get('username', '')

    context_dict = {
        'u': u,
    }

    for k, y in request.GET.items():
        print(k, y)
    return render(request,
                  'blog/homepage.html',
                  context=context_dict
                  )


def sign_up_view(request):
    context_dict = {
    }

    return render(request,
                  'blog/sign_up.html',
                  context=context_dict
                  )


def create_new_user(request):
    context_dict = {
    }

    # transfer english error msg to Chinese
    error_dict = {
        'This password is too short. It must contain at least 6 characters.': '密码少于6位',
        'This password is too common.': '密码太简单',
        'This password is entirely numeric.': '密码是纯数字'
    }

    # get form data from POST
    post = request.POST
    username = post['username']
    password = post['password']

    try:
        validate_password(password=password)
        validate_username(username)
    except exceptions.ValidationError as error_msg:
        context_dict['error_msg'] = [error_dict.get(e, e) for e in error_msg]
        return render(request,
                      'blog/sign_up.html',
                      context=context_dict
                      )
    else:
        password = make_password(password, 'bgztech')
        u = Users(username=username, password=password)
        u.save()
        return HttpResponseRedirect(reverse('homepage'))


def sign_in(request):
    context_dict = {
    }
    return render(request,
                  'blog/sign_in.html',
                  context=context_dict,
                  )


def sign_in_check(request):
    context_dict = {
    }
    flag = False

    post = request.POST
    username = post['username']
    password = post['password']

    # find user and validate password
    user = Users.objects(username=username).first()
    if user is not None:
        flag = check_password(password, user.password)

    if not flag:
        context_dict['error_msg'] = ['账号/密码错误']
        return render(request,
                      'blog/sign_in.html',
                      context=context_dict,
                      )
    else:
        context_dict['error_msg'] = ['登录成功']

        response = render(request,
                          'blog/sign_in.html',
                          context=context_dict,
                          )
        response.set_cookie('username', username)

        return response
