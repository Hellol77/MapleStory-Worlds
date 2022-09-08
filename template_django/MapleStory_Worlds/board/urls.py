# users/urls.py

from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('register/', views.PostUpload, name='register'),
    path('check/', views.CheckView, name='register'),
    path('check/mission_show', views.mission_show),
    path('check/mission_show_semi', views.mission_show_semi),
    path('detail/<int:pk>', views.DetailView, name='detail'),
    path('detail/<int:pk>/delete/', views.mission_delete, name='delete'),
    path('register/<int:pk>/edit/', views.mission_edit, name='edit'),
]