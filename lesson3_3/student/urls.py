from django.urls import path
from .views import get_student

urlpatterns = [
    path('student/', get_student),
]