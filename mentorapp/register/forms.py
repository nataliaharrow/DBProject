from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from app_user.models import User, School, Industry, Major, Request, Company
from django.db.utils import OperationalError, ProgrammingError


# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column


class StudentRegisterForm(UserCreationForm):
    email = models.EmailField()

    try:
        school = forms.CharField(label='School', widget=forms.Select(
            choices=School.objects.all().values_list('id', 'school_name')), required=True)
    except OperationalError:
        school = forms.CharField(max_length=20, required=False)
    except ProgrammingError:
        school = forms.CharField(max_length=20, required=False)

    try:
        major = forms.CharField(label='Major', widget=forms.Select(
            choices=Major.objects.all().values_list('id', 'major_name')), required=True)
    except OperationalError:
        major = forms.CharField(max_length=20, required=False)
    except ProgrammingError:
        major = forms.CharField(max_length=20, required=False)

    try:
        industry = forms.CharField(label='Industry', widget=forms.Select(
            choices=Industry.objects.all().values_list('id', 'industry_type_name')), required=True)
    except OperationalError:
        industry = forms.CharField(max_length=20, required=False)
    except ProgrammingError:
        industry = forms.CharField(max_length=20, required=False)

    requests = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), widget=forms.CheckboxSelectMultiple,
                                            required=True, label='What you need help with:')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "school", "major",
                  "requests", "industry"]


class MentorRegisterForm(UserCreationForm):
    email = models.EmailField()
    # company = forms.CharField(max_length=25, required=True)
    positions = forms.CharField(max_length=25, required=True, label='Position')

    try:
        school = forms.CharField(label='School', widget=forms.Select(
            choices=School.objects.all().values_list('id', 'school_name')), required=True)
    except OperationalError:
        school = forms.CharField(max_length=20, required=False)
    except ProgrammingError:
        school = forms.CharField(max_length=20, required=False)

    try:
        major = forms.CharField(label='Major', widget=forms.Select(
            choices=Major.objects.all().values_list('id', 'major_name')), required=True)
    except OperationalError:
        major = forms.CharField(max_length=20, required=False)
    except ProgrammingError:
        major = forms.CharField(max_length=20, required=False)

    try:
        industry = forms.CharField(label='Industry', widget=forms.Select(
            choices=Industry.objects.all().values_list('id', 'industry_type_name')), required=True)
    except OperationalError:
        industry = forms.CharField(max_length=20, required=False)
    except ProgrammingError:
        industry = forms.CharField(max_length=20, required=False)

    try:
        company = forms.CharField(label='Company', widget=forms.Select(
            choices=Company.objects.all().values_list('id', 'company_name')), required=True)
    except OperationalError:
        company = forms.CharField(max_length=20, required=False)
    except ProgrammingError:
        company = forms.CharField(max_length=20, required=False)

    requests = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), widget=forms.CheckboxSelectMultiple,
                                              required=True, label='What you need help with:')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "school", "major",
                  "requests", "industry", "company", "positions"]




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