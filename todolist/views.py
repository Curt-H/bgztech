from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from blog import current_user, get_from_cookies


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


def new(request):
    return HttpResponse('new')


def new_get(request):
    return HttpResponse('new_get')


def new_post(request):
    return HttpResponse('new_post')
