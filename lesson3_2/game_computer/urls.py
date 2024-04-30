from django.urls import path
from .views import get_info

urlpatterns = [
    path('game_c/', get_info),
]