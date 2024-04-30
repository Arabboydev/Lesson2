from django.shortcuts import render
from django.http import HttpResponse


def get_info(request):
    return HttpResponse('Hello car page')
# Create your views here.
