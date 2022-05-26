from django.shortcuts import render
from Applications.routes.models import Route

def all_routes(request):
    routes = Route.objects.all()
    return render(request, "routes/all_routes.html", {'routes': routes})