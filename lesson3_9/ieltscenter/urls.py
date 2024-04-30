from django.urls import path
from .views import get_ielts

urlpatterns = [
    path('ielts/', get_ielts),
]
