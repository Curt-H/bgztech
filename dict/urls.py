from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from dict import views

urlpatterns = [
                  path('dict', views.dictionary, name='router'),
                  path('dict/new', views.show_add_word_form, name='new word form'),
                  path('dict/new/add', views.add_new_word, name='add new word'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
