# todo/urls.py

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),
    path('task', views.task_list, name='task_list'),  # List all tasks
    path('task/<int:pk>/', views.task_detail, name='task_detail'),  # Add a new task
    path('task/add/', views.task_create, name='task_create'),  # View details of a specific task
    path('task/<int:pk>/update/', views.task_update, name='task_update'),  # Update a task
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),  # Delete a task
]
