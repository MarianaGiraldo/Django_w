from django.shortcuts import render

def all_buses(request):
    buses = None
    return render(request, "buses/all_buses.html", {'buses': buses})

def insert_bus(request):
    return render(request, "buses/insert_bus.html", {})

def edit_bus(request, id):
    return render(request, "buses/edit_bus.html", {})
