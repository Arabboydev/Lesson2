from django.shortcuts import render
from django.http import HttpResponse


def get_student(request):
    return HttpResponse('<h1>This is student page<h1/>')
