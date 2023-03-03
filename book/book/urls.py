from django.contrib import admin
from django.urls import path, include
from books import views
from lessonApp.views import get_task_by_id, get_tasks, create_task, update_task, delete_task

urlpatterns = [
    # library
    path('admin/', admin.site.urls),
    path('api/v1/', views.api_overview, name='apiOverview'),
    path('api/v1/get_books/', views.get_books, name='books'),
    path('api/v1/get_book/<int:pk>/', views.get_book, name='book'),
    path('api/v1/create_book/', views.create_book, name='create_book'),
    path('api/v1/delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('api/v1/update_book/<int:pk>/', views.update_book, name='update_book'),
    # tasks
    path('task/<int:pk>/', get_task_by_id),
    path('tasks/', get_tasks),
    path('create_task/', create_task),
    path('update_task/<int:pk>/', update_task),
    path('delete_task/<int:pk>/', delete_task),
]
