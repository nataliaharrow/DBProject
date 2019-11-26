from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# Inherit from UserCreationForm and modify the form
class RegisterForm(UserCreationForm):
    email = models.EmailField()

    # change parent properties of the class
    class Meta:
        model = User
        student_check_box = forms.CheckboxInput(check_test="Student")
        mentor_check_box = forms.CheckboxInput(check_test="Mentor")
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


