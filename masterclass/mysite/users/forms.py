from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # the meta class is used to configure the form; it provides information about the class itself
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
