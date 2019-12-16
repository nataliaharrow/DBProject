from django.urls import path

from . import views

urlpatterns = [
    path('requests/', views.requests, name='requests'),
    path('upload/', views.upload, name='upload'),
    path('<int:pk>/', views.delete_request, name='delete_request'),

]
