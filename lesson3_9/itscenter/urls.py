from django.urls import path
from .views import get_it

urlpatterns = [
    path('it/', get_it),
]