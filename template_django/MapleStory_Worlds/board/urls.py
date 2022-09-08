# users/urls.py

from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('register/', views.PostUpload, name='register'),
    path('check/', views.DetailView, name='register'),
    path('check/mission_show', views.mission_show),
    path('check/mission_show_semi', views.mission_show_semi),
]