from django.shortcuts import render
from django.http import HttpResponse


def get_it(request):
    return HttpResponse('This is it center page')

