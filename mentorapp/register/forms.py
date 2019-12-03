from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from app_user.models import User, School, Industry, Major, Request

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column

class StudentRegisterForm(UserCreationForm):
    email = models.EmailField()
    school = forms.CharField(label='School', widget=forms.Select(choices=School.SCHOOL_CHOICES), required=True)
    major = forms.CharField(label='Major', widget=forms.Select(choices=Major.MAJOR_CHOICES), required=True)
    industry = forms.CharField(label='Industry you\'re interested in:', widget=forms.Select(choices=Industry.INDUSTRY_TYPE_CHOICES),
                               required=True)
    requests = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), widget=forms.CheckboxSelectMultiple,
                                              required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "school", "major",
                  "requests", "industry"]


class MentorRegisterForm(UserCreationForm):
    email = models.EmailField()
    school = forms.CharField(label='School', widget=forms.Select(choices=School.SCHOOL_CHOICES),required=False)
    major = forms.CharField(label='Major', widget=forms.Select(choices=Major.MAJOR_CHOICES), required=False)
    company = forms.CharField(max_length=25, required=True)
    positions = forms.CharField(max_length=25, required=True, label='Position')
    industry = forms.CharField(label='Industry', widget=forms.Select(choices=Industry.INDUSTRY_TYPE_CHOICES),required=True)
    requests = forms.ModelMultipleChoiceField(queryset=Request.objects.all(), widget=forms.CheckboxSelectMultiple,
                                              required=True, label='Can help students with:')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "school", "major", "requests", "industry", "company", "positions"]




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