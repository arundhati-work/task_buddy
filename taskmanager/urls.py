from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('tasks/',views.task_list, name="task_list"),
    path('tasks/new/', views.create_task, name="create_task"),
    path('tasks/<int:task_id>/', views.task_detail, name="task_detail"),
    path('tasks/edit/<int:task_id>/', views.edit_task, name="edit_task"),
]