from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.shortcuts import render


# Create your views here.


def index(request):
    context_dict = {
    }
    return render(request,
                  'blog/index.html',
                  context=context_dict
                  )


def homepage(request):
    context_dict = {
    }

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
    error_list = {
        'This password is too short. It must contain at least 6 characters.': '密码少于6位',
        'This password is too common.': '密码太简单',
        'This password is entirely numeric.': '密码是纯数字'
    }

    post = request.POST

    try:
        validate_password(password=post['password'])
    except exceptions.ValidationError as error_msg:
        context_dict['error_msg'] = [error_list[e] for e in error_msg]
        return render(request,
                      'blog/sign_up.html',
                      context=context_dict
                      )
    else:
        print(post)
        print(post['password'])
        return render(request,
                      'blog/sign_up.html',
                      )
