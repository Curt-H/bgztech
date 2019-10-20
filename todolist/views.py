from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# Create your views here.
from todolist.models import Todo
from utils.utils import log


def homepage(request):
    context_dict = dict()

    todos = Todo.objects

    for i in range(len(todos)):
        todos[i].id = str(todos[i].id)
        print(todos[i].id)
        print(type(todos[i].id))
    context_dict['todos'] = todos
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
    todo = Todo()
    data = todo.get_data_from_request(request)
    log(f'Recieved data {data}')
    todo.new(data)

    return redirect(reverse(homepage))


def todo_content(request, todo_id):
    context_dict = dict()
    context_dict.todo_id = todo_id

    return render(request,
                  'todolist/new_view.html',
                  context=context_dict
                  )
