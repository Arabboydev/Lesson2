from django.urls import path
from .views import get_women

urlpatterns = [
    path('women/', get_women),
]