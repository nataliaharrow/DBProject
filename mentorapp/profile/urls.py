from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.profile, name='profile'),
    path('edit/', views.edit, name='edit')
]
