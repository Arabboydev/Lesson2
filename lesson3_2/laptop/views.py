from django.shortcuts import render
from django.http import HttpResponse


def get_index(request):
    return HttpResponse('<h1>This is index page <h1/>')
# Create your views here.
