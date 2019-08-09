from django.shortcuts import render


# Create your views here.

def index(request):
    context_dict = {
    }
    return render(request,
                  'blog/index.html',
                  context=context_dict
                  )


def homepage(request):
    context_dict = {
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


def test_post(request):
    post = {**request.POST}
    print(post)
    return render(request,
                  'blog/sign_up.html',
                  )
