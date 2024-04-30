from django.urls import path
from .views import get_tv

urlpatterns = [
    path('tv/', get_tv),
]