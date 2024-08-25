from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by("-updated_at")
    completed_tasks = Task.objects.filter(is_completed=True).order_by("-updated_at")
    return render(request, "home.html", context={"tasks123": tasks, "completed_tasks": completed_tasks})



##### Test code #####
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, World!")
