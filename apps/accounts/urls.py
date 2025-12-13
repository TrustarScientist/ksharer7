from django.urls import path

from apps.accounts.views import register, login, logout


# Create your views here.

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]