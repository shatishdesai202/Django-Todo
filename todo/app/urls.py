from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo_delete/<id>', views.todo_delete, name="todo_delete"),
    path('todo_update/<id>', views.todo_update, name="todo_update"),
    path('todo_delete_complete', views.todo_delete_complete, name="todo_delete_complete"),
    path('todo_delete_all', views.todo_delete_all, name="todo_delete_all"),
    path('back_to_home', views.back_to_home, name="back_to_home"),
]
