from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.password_validation import validate_password
from django.contrib.sessions.models import Session
from django.core import exceptions
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from blog import validate_username, Users, set_session, current_user, create_user, find_user


def index(request):
    context_dict = {
    }
    return render(request,
                  'blog/index.html',
                  context=context_dict
                  )


def homepage(request):
    u = current_user(request)
    context_dict = {
        'u': u,
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


def create_new_user(request):
    context_dict = {
    }

    result = create_user(request)

    if not result['success']:
        context_dict['error_msg'] = result['error_msg']
        return render(request,
                      'blog/sign_up.html',
                      context=context_dict
                      )
    else:
        response = HttpResponseRedirect(reverse('homepage'))
        set_session(response, result['user'])
        return response


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

    find, user = find_user(request)
    if not find:
        context_dict['error_msg'] = ['账号/密码错误']
        return render(request,
                      'blog/sign_in.html',
                      context=context_dict,
                      )
    else:
        response = HttpResponseRedirect(reverse('homepage'))
        set_session(response, user)
        return response


def show_article(request, *args):
    return None