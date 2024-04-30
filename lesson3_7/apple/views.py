from django.shortcuts import render
from django.http import HttpResponse


def get_iphone(request):
    return HttpResponse('This is apple page')
# Create your views here.
