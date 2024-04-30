from django.urls import path
from .views import get_samsung

urlpatterns = [
    path('samsung/', get_samsung),
]
