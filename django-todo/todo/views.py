from multiprocessing import context
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse    
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    # The remaining fields of the task model are either automatically filled or have default values(is_completed=False)
    # return HttpResponse('The form was submitted')
    return redirect("home")
    

def mark_as_done(request, pk):
    # return HttpResponse(f"Mark as done: {pk}")
    task = get_object_or_404(Task, pk=pk)
    # return HttpResponse(task)
    task.is_completed = True
    task.save()
    return redirect("home")


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect("home")


def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task = request.POST["task"]
        get_task.task = new_task
        get_task.save()
        return redirect("home")
    else:
        context = {
            "get_task": get_task
        }
        return render(request, "edit_task.html", context)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")