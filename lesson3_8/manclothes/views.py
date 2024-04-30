from django.shortcuts import render
from django.http import HttpResponse


def get_man(request):
    return HttpResponse("This is man clothes page")
# Create your views here.
