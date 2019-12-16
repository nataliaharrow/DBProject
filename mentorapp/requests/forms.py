from django import forms

from app_user.models import UserRequest


class RequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ('requesting', 'description','document',)