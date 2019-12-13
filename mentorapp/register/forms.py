from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from app_user.models import User, School, Industry, Major, Request, Company


# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column


class StudentRegisterForm(UserCreationForm):
    email = models.EmailField()

    try:
        school = forms.CharField(max_length=30, required=True, label='School')
    except:
        school = forms.CharField(max_length=30, required=False)

    try:
        major = forms.CharField(max_length=30, required=True, label='Major')
    except:
        major = forms.CharField(max_length=30, required=False)

    try:
        industry = forms.CharField(max_length=30, required=False, label='Industry')
    except:
        industry = forms.CharField(max_length=30, required=False)

    # requests = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), widget=forms.CheckboxSelectMultiple,
    #                                         required=True, label='What you need help with:')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "school", "major", "industry"]


class MentorRegisterForm(UserCreationForm):
    email = models.EmailField()

    positions = forms.CharField(max_length=25, required=True, label='Position')

    try:
        school = forms.CharField(max_length=20, required=False, label='School')
    except:
        school = forms.CharField(max_length=20, required=False)

    try:
        major = forms.CharField(max_length=20, required=False, label='Major')
    except:
        major = forms.CharField(max_length=20, required=False)

    try:
        industry = forms.CharField(max_length=20, required=True, label='Industry')
    except:
        industry = forms.CharField(max_length=20, required=False)

    try:
        company = forms.CharField(max_length=20, required=True, label='Company')

    except:
        company = forms.CharField(max_length=20, required=False)

    # requests = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), widget=forms.CheckboxSelectMultiple,
    #                                           required=True, label='What you can help with:')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "school", "major", "industry", "company", "positions"]




# # Inherit from UserCreationForm and modify the form
# class StudentRegisterForm(UserCreationForm):
#     email = models.EmailField()
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
#
#
# class MentorRegisterForm(UserCreationForm):
#     email = models.EmailField()
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


# class MentorRegisterForm(forms.ModelForm):
#     mentor = forms.BooleanField(required=False)
#
#     class Meta:
#         model = Mentor
#         fields = ('mentor',)
#