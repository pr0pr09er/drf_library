from django.urls import path
from .views import get_task_by_id, get_tasks, create_task, update_task, delete_task

urlpatterns = [
    path('task/<int:pk>/', get_task_by_id),
    path('tasks/', get_tasks),
    path('create_task/', create_task),
    path('update_task/<int:pk>/', update_task),
    path('delete_task/<int:pk>/', delete_task),
]
