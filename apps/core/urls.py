from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('feed/', views.feed, name='feed'),
    path('resources/', views.resources, name='resources'),
    path('messaging/', views.messaging, name='messaging'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    
]