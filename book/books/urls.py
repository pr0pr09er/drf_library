from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='apiOverview'),
    path('get_books/', views.get_books, name='books'),
    path('get_book/<int:pk>/', views.get_book, name='book'),
    path('create_book/', views.create_book, name='create_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('update_book/<int:pk>/', views.update_book, name='update_book'),
]
