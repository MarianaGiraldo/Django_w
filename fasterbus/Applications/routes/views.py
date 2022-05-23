from django.shortcuts import render

def all_routes(request):
    routes = None
    return render(request, "routes/all_routes.html", {'routes': routes})