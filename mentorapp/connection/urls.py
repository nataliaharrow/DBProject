from django.urls import path

from . import views

urlpatterns = [
    path('connections/', views.connections, name="connections"),
    path('pending/', views.pending, name="pending"),
]