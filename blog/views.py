from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    context_dict = {
        'arg': '123',
    }
    return render(request,
                  'blog/index.html',
                  context=context_dict
                  )
