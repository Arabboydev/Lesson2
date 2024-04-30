from django.urls import path
from .views import get_man

urlpatterns = [
    path('man/', get_man),
]