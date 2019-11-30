from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from app_user.models import User

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column


# Inherit from UserCreationForm and modify the form
class StudentRegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class MentorRegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


# class MentorRegisterForm(forms.ModelForm):
#     mentor = forms.BooleanField(required=False)
#
#     class Meta:
#         model = Mentor
#         fields = ('mentor',)
#