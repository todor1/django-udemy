from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm
from django.contrib.auth import logout

# from django.contrib.auth.forms import UserCreationForm

# Django offers authentication views & html template out of the box.
# We can use these views to create a login page.


def register(request):
    if request.method == "POST":
        ## form = UserCreationForm(request.POST)
        ## extended form containing email field
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                # request, f"Welcome, {username}. Your account has been created."
                request,
                f"Welcome, {username}!",
            )
            # return redirect("food:index")
            return redirect("login")
    else:
        ## form = UserCreationForm()
        ## extended form containing email field
        form = RegisterForm()
    return render(request, "users/register.html", context={"form": form})


def logout_view(request):
    logout(request)
    return render(request, "users/logout.html")
