from django.shortcuts import render
from django.http import HttpResponse

def in_news(request):
    return HttpResponse('Hi, you are at the \"news\"')
