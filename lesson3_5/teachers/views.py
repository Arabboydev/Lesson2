from django.shortcuts import render
from django.http import HttpResponse


def get_teacher(request):
    return HttpResponse("This is teacher page")
# Create your views here.
