from django.shortcuts import render
from django.http import HttpResponse


def get_samsung(request):
    return HttpResponse('This is samsung page')