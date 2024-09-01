from multiprocessing import context
from django.shortcuts import redirect, render
from .models import List
from .forms import ListForm
from django.contrib import messages


def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            tasks = List.objects.all()
            messages.success(request, "Task has been added!")
            return render(request, "home.html", {"tasks": tasks})
    else:
        tasks = List.objects.all()
        return render(request, "home.html", {"tasks": tasks})


def about(request):
    context = {"first_name": "John", "last_name": "Doe"}
    return render(request, "about.html", context=context)


def delete(request, list_id: int):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, f"Task {item.item} has been deleted!")
    return redirect("home")


def cross_off(request, list_id: int):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect("home")


def uncross(request, list_id: int):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect("home")


def edit(request, list_id: int):
    if request.method == "POST":
        task_edited = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=task_edited)
        if form.is_valid():
            form.save()
            messages.success(request, "Item has been edited!")
            return redirect("home")
    else:
        task_edited = List.objects.get(pk=list_id)
        return render(request, "edit.html", {"task_edited": task_edited})
