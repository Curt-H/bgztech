from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# Create your views here.
from blog import current_user, get_from_cookies
from utils import log


def homepage(request):
    context_dict = dict()

    session_id = get_from_cookies(request, 'session_id')
    user = current_user(session_id)

    context_dict['user'] = user
    return render(request,
                  'todolist/homepage.html',
                  context=context_dict
                  )


def edit(request):
    return HttpResponse('edit')


def edit_get(request):
    return HttpResponse('edit_get')


def edit_post(request):
    return HttpResponse('edit_post')


def new_view(request):
    context_dict = dict()

    return render(request,
                  'todolist/new_view.html',
                  context=context_dict
                  )


def new_submit(request):
    log('activate')
    post = dict(request.POST)
    for k, v in post.items():
        log(f'{k} = {v}')
    return redirect(reverse(new_view))
