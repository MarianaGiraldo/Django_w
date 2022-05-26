from django.shortcuts import render, redirect
from .models import Bus
from .forms import BusForm

def all_buses(request):
    buses = Bus.objects.all()
    return render(request, "buses/all_buses.html", {'buses': buses})

def insert_bus(request):
    if request.method == 'GET' :
        form = BusForm()
    else:
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_buses")
    return render(request, "buses/insert_bus.html", { 'form': form })

def edit_bus(request, id):
    bus = Bus.objects.get( id = id )
    if request.method == 'GET' :
        form = BusForm( instance = bus )
    else:
        form = BusForm( request.POST,  instance = bus )
        if form.is_valid():
            form.save()
            return redirect("all_buses")
    return render(request, "buses/insert_bus.html", { 'form': form })

def delete_bus(request, id):
    bus = Bus.objects.get( id = id )
    bus.delete()
    return redirect("all_buses")
