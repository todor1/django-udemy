from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Django offers authentication views & html template out of the box.
# We can use these views to create a login page.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Welcome, {username}. Your account has been created."
            )
            return redirect("food:index")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", context={"form": form})
