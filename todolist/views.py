from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# Create your views here.
from todolist import bgz_checked
from todolist.models import Todo
from utils.utils import log


@bgz_checked
def homepage(request):
    context_dict = dict()

    todos = Todo.objects

    context_dict['todos'] = todos
    return render(request,
                  'todolist/homepage.html',
                  context=context_dict
                  )


@bgz_checked
def edit(request):
    return HttpResponse('edit')


@bgz_checked
def edit_get(request):
    return HttpResponse('edit_get')


@bgz_checked
def edit_post(request):
    return HttpResponse('edit_post')


@bgz_checked
def new_view(request):
    context_dict = dict()

    return render(request,
                  'todolist/new_view.html',
                  context=context_dict
                  )


@bgz_checked
def new_submit(request):
    todo = Todo()
    data = todo.get_data_from_request(request)
    log(f'Recieved data {data}')
    todo.new(data)

    return redirect(reverse(homepage))


@bgz_checked
def todo_content(request, todo_id):
    context_dict = dict()
    todo_uuid = str(todo_id)
    todo = Todo.objects(uuid=todo_uuid).first()
    log(todo)
    context_dict['todo'] = todo

    return render(request,
                  'todolist/todo_content.html',
                  context=context_dict
                  )


@bgz_checked
def todo_delete(request, todo_id):
    context_dict = dict()
    todo_uuid = str(todo_id)
    todo = Todo.objects(uuid=todo_uuid).first()
    log(f'开始执行删除, 被删除任务ID:{todo.id}')
    todo.delete()

    return redirect(reverse(homepage))


@bgz_checked
def todo_finish(request, todo_id):
    context_dict = dict()
    todo_uuid = str(todo_id)
    todo = Todo.objects(uuid=todo_uuid).first()

    log(f'开始递交任务完成回执, 任务ID:{todo.id}')

    todo.finish = True
    todo.save()

    log(f'任务完成回执递交完成, 任务ID:{todo.id}')

    return redirect(reverse(homepage))
