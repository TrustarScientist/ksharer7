from django.urls import path

from apps.core.views import homepage

# Create your views here.

urlpatterns = [
    path('', homepage, name='homepage'),
]