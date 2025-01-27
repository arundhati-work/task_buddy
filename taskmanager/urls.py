from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('tasks/',views.task_list, name="task_list"),
    path('tasks/new/', views.create_task, name="create_task"),
    path('tasks/<int:task_id>/', views.task_detail, name="task_detail"),
    path('tasks/edit/<int:task_id>/', views.edit_task, name="edit_task"),
    path('tasks/delete/<int:task_id>/', views.delete_task, name="delete_task"),
    path('tasks/complete/<int:task_id>/', views.complete_task, name="complete_task"),
    path('tasks/incomplete/<int:task_id>/', views.unmark_complete_task, name="unmark_complete_task"),
]