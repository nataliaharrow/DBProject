from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Inherit from UserCreationForm and modify the form
class RegisterForm(UserCreationForm):
    email = models.EmailField()

    # change parent properties of the class
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

