from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return HttpResponse('homepage')


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
