from django.conf.urls.static import static
from django.urls import path

from bgztech import settings
from todolist import views

urlpatterns = [
                  path('todo', views.homepage, name='todo homepage'),
                  path('todo/new', views.new_view, name='todo new view'),
                  path('todo/new/view', views.new_view, name='todo new view'),
                  path('todo/new/submit', views.new_submit, name='todo new post'),
                  path('todo/edit', views.edit, name='todo edit'),
                  path('todo/<str: todo_id>', views.todo_content, name='todo content'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
