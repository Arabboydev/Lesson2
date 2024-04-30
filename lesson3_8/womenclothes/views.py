from django.shortcuts import render
from django.http import HttpResponse


def get_women(request):
    return HttpResponse("This is women clothes page")
# Create your views here.
