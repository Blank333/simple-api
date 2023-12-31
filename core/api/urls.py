from django.urls import path
from .views import TodoListApiView, TodoApiView

urlpatterns = [
    path('todos/', TodoListApiView.as_view()),
    path('todos/<int:todo_id>', TodoApiView.as_view()),
]