from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('student_register/', views.student_register, name='student_register'),
    path('mentor_register/', views.mentor_register, name='mentor_register'),
]
