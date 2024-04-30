from django.shortcuts import render
from django.http import HttpResponse


def get_tv(request):
    return HttpResponse("This is tv page")