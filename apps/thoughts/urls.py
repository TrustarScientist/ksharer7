from django.urls import path

from . import views

app_name = 'thoughts'

urlpatterns = [
    path('create/', views.create_thought, name='create_thought'),
]