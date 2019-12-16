from django import forms
from app_user.models import *

# class UserForm(forms.ModelForm):
#     class Meta:
#         model= User
#         fields=[
#             'email',
#             'first_name',
#             'last_name',
#         ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=[ 
            # 'bio',
            # 'website',
            'image',
            ]