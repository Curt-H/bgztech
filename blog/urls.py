from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('homepage/', views.homepage, name='homepage'),
                  path('homepage/<u>', views.homepage, name='homepage'),
                  path('signup/', views.sign_up_view, name='sign up'),
                  path('signup/validate', views.create_new_user, name='register'),
                  path('signin', views.sign_in, name='sign in'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
