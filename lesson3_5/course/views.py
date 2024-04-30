from django.shortcuts import render
from django.http import HttpResponse


def get_student(request):
    return HttpResponse("This is student page")