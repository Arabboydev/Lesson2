from django.shortcuts import render
from django.http import HttpResponse


def get_techer(request):
    return HttpResponse('<h1>This is teacher page<h1/>')

# Create your views here.
