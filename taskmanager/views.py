from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required
def task_list(request):
    tasks = Task.objects.filter(author=request.user)
    context = {
        "tasks":tasks
    }
    return render(request, "taskmanager/task_list.html", context)

def create_task(request):
    if request.method=="GET":
        form = TaskForm()
        context = {
            "form":form,
            "task": None
        }
        return render(request, "taskmanager/task_form.html",context)
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect("task_list")
        else:
            context = {
            "form":form,
            "task" : None
            }
            return render(request, "taskmanager/task_form.html",context)

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {
        "task" : task
    }
    return render(request, "taskmanager/task_detail.html", context)

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method=="GET":
        form = TaskForm(instance=task)
        context = {
            "form": form,
            "task":task
        }
        return render(request, "taskmanager/task_form.html", context)
    else:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task_instance = form.save()
            return redirect("task_detail", task_id=task_instance.id)
        else:
            context = {
                "form": form,
                "task":task
            }
            return render(request, "taskmanager/task_form.html", context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method=="GET":
        context = {
            "task":task
        }
        return render(request, "taskmanager/delete_task.html", context)
    else:
        task.delete()
        return redirect("task_list")


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect("task_list")

def unmark_complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = False
    task.save()
    return redirect("task_list")