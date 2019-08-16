from django.shortcuts import render
from dict.models import Dict


# Create your views here.


def dictionary(request):
    context_dict = dict()

    words = [i for i in Dict.objects.all()]
    context_dict["words"] = words
    return render(request,
                  'blog/dict.html',
                  context=context_dict
                  )
