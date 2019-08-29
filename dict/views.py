from django.shortcuts import render, redirect
from django.urls import reverse

from dict.models import Dict, Content


# Create your views here.


def dictionary(request):
    context_dict = dict()

    words = [i for i in Dict.objects.all()]
    context_dict["words"] = words
    return render(request,
                  'blog/dict.html',
                  context=context_dict
                  )


def show_add_word_form(request):
    context_dict = dict()

    return render(request,
                  'blog/new_word_form.html',
                  context=context_dict
                  )


def add_new_word(request):
    context_dict = dict()
    post = request.POST

    dict_book = Dict()
    dict_book.word = post.get('word')
    paraphrase = Content()
    paraphrase.part_of_speech = post.get('part_of_speech')
    paraphrase.paraphrase = post.get('paraphrase')
    paraphrase.example = post.get('example')
    dict_book.paraphrase.append(paraphrase)
    dict_book.save()

    c = dict_book.paraphrase[0]
    print(c.part_of_speech)
    return redirect(reverse("router"))
