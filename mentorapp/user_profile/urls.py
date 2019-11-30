from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_user_profile, name='profile'),
]
