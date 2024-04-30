from django.urls import path
from .views import get_technique


urlpatterns = [
    path('tech/', get_technique),
]
