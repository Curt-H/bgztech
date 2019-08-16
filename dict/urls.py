from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from dict import views

urlpatterns = [
                  path('dict', views.dictionary, name='router'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
