# users/urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'board'

urlpatterns = [
    path('register/', views.PostUpload, name='register'),
    path('check/', views.CheckView, name='register'),
    path('check/mission_show', views.mission_show),
    path('check/mission_show_semi', views.mission_show_semi),

    path('detail/M1/<int:pk>', views.DetailView_M1, name='detail'),
    path('detail/M2/<int:pk>', views.DetailView_M2, name='detail'),
    path('detail/M3/<int:pk>', views.DetailView_M3, name='detail'),
    path('detail/M4/<int:pk>', views.DetailView_M4, name='detail'),
    path('detail/M5/<int:pk>', views.DetailView_M5, name='detail'),

    path('detail/M1/<int:pk>/delete/', views.mission_delete_M1, name='delete'),
    path('detail/M2/<int:pk>/delete/', views.mission_delete_M2, name='delete'),
    path('detail/M3/<int:pk>/delete/', views.mission_delete_M3, name='delete'),
    path('detail/M4/<int:pk>/delete/', views.mission_delete_M4, name='delete'),
    path('detail/M5/<int:pk>/delete/', views.mission_delete_M5, name='delete'),

    path('register/M1/<int:pk>/edit/', views.mission_edit_M1, name='edit'),
    path('register/M2/<int:pk>/edit/', views.mission_edit_M2, name='edit'),
    path('register/M3/<int:pk>/edit/', views.mission_edit_M3, name='edit'),
    path('register/M4/<int:pk>/edit/', views.mission_edit_M4, name='edit'),
    path('register/M5/<int:pk>/edit/', views.mission_edit_M5, name='edit'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)