from django.shortcuts import render


# Create your views here.


def dictionary(request):
    context_dict = dict()

    return render(request,
                  'blog/dict.html',
                  context=context_dict
                  )
