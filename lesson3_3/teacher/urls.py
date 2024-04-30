from django.urls import path
from .views import get_techer

urlpatterns = [
    path('teacher/', get_techer),
]