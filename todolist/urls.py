from django.conf.urls.static import static
from django.urls import path

from bgztech import settings
from todolist import views

urlpatterns = [
                  path('todo', views.homepage, name='todo homepage'),
                  path('todo/new', views.new, name='todo new'),
                  path('todo/edit', views.edit, name='todo edit'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
