from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_student_profile, name='student_profile'),
]

