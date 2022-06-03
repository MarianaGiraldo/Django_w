from django.shortcuts import render, redirect
from .models import Route
from .forms import RouteForm

def all_routes(request):
    routes = Route.objects.all()
    return render(request, "routes/all_routes.html", {'routes': routes})

def insert_route(request):
    if request.method == 'GET' :
        form = RouteForm()
    else:
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_routes")
    return render(request, "routes/form_route.html", { 'form': form })

def edit_route(request, id):
    route = Route.objects.get( id = id )
    if request.method == 'GET' :
        form = RouteForm( instance = route )
    else:
        form = RouteForm( request.POST,  instance = route )
        if form.is_valid():
            form.save()
            return redirect("all_routes")
    return render(request, "routes/form_route.html", { 'form': form })

def delete_route(request, id):
    route = Route.objects.get( id = id )
    route.delete()
    return redirect("all_routes")

