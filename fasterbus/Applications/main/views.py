from django.http import HttpResponse
from django.shortcuts import render

def title(request):
    return HttpResponse("<h1>Hello world</h1>")

def index(request):
    return render(request, "index.html")

def param(request, num, name):
    return HttpResponse(f"<h1>Num: {num} </h1> <h1>Name: {name} </h1>")
