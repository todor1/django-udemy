from math import e
import re
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()
    # check if the user is logged in
    if request.method == "POST":
        # get the user's input (name property of the input field)
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        # check if the user is authenticated
        if user is not None:
            # login the user
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("home")
    else:
        # if the user is not posting data, return the home page
        return render(request, "home.html", {"records": records})


###########################################################################
### naming the login and logout functions differently to avoid conflicts with the built-in Django functions

# def login_user(request):
#    pass
### implemented in the home function above


def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out.")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


###########################################################################


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up records by primary key
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.error(request, "You need to be logged in to view this page.")
        return redirect("home")


# def delete_record(request, pk):
#     # Original code without confirmation
#     if request.user.is_authenticated:
#         # Look up records by primary key
#         record_to_delete = Record.objects.get(id=pk)
#         if record_to_delete:
#             record_to_delete.delete()
#             messages.success(request, "Record deleted.")
#             return redirect("home")
#     else:
#         messages.error(request, "You need to be logged in to delete a record.")
#         return redirect("home")


def delete_record(request, pk):
    # Confirmation berfore deleting a record
    # https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349788-delete-objects-safely-with-user-confirmation
    if request.user.is_authenticated:
        # Look up records by primary key
        record_to_delete = Record.objects.get(id=pk)
        if record_to_delete:
            if request.method == "POST":
                record_to_delete.delete()
                messages.success(request, "Record deleted.")
                return redirect("home")
            return render(
                request,
                "delete_record.html",
                context={"record_to_delete": record_to_delete},
            )
    else:
        messages.error(request, "You need to be logged in to delete a record.")
        return redirect("home")


def add_record(request):
    # check if the user os posting daata, if not return a web page
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added.")
                return redirect("home")
        return render(request, "add_record.html", context={"form": form})
    else:
        messages.error(request, "You need to be logged in to add a record.")
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        # populate the form with the current record: instance=current_record
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated.")
            return redirect("home")
        else:
            return render(request, "update_record.html", context={"form": form})
    else:
        messages.error(request, "You need to be logged in to update a record.")
        return redirect("home")
