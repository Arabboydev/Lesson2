from django.shortcuts import render
from django.http import HttpResponse


def get_info(request):
    return HttpResponse('This is game computer page')
# Create your views here.
