from django.shortcuts import render
from django.http import HttpResponse


def get_ielts(request):
    return HttpResponse('This is ielts center page')
