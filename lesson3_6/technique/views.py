from django.shortcuts import render
from django.http import HttpResponse


def get_technique(request):
    return HttpResponse("This is technique page")
# Create your views here.
