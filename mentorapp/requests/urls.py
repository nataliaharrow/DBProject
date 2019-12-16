from django.urls import path

from . import views

urlpatterns = [
    path('', views.requests, name='requests'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('respond/<int:pk>/', views.respond, name='respond'),
]
