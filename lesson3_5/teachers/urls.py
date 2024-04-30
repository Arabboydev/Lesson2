from django.urls import path
from .views import get_teacher


urlpatterns = [
    path('teacher/', get_teacher),
]