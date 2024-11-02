import re
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
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
        return render(request, "home.html", {})


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
    return render(request, "register.html", {})


###########################################################################
