from django.urls import path
from .views import get_iphone

urlpatterns = [
    path('apple/', get_iphone),
]
