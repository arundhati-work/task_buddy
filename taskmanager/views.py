from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):
    return render(request, "home.html")

def task_list(request):
    tasks = Task.objects.all()
    context = {
        "tasks":tasks
    }
    return render(request, "taskmanager/task_list.html", context)