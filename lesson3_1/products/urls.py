from django.urls import path
from .views import get_info


urlpatterns = [
    path('cars', get_info),
]