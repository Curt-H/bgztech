from django.contrib.auth.hashers import make_password
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
    context_dict = {
        'u': u,
    }
    print(request.GET)
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


def test_post(request):
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
