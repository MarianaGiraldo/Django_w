from django.http import HttpResponse
from django.shortcuts import render

def title(request):
    return HttpResponse("<h1>Hello world</h1>")

def index(request):
    return HttpResponse("<h1>Faster Bus index</h1>")
