import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse    
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    # The remainig fields of the task model are either automatically filled or have default values(is_completed=False)
    Task.objects.create(task=task)
    # return HttpResponse('The form was submitted')
    return redirect("home")
    

def mark_as_done(request, pk):
    # return HttpResponse(f"Mark as done: {pk}")
    task = get_object_or_404(Task, pk=pk)
    # return HttpResponse(task)
    task.is_completed = True
    task.save()
    return redirect("home")