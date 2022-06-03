from django.shortcuts import render, redirect

from Applications.routes.models import Route
from Applications.buses.models import Bus
from .models import Ticket
from .forms import TicketForm

def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/all_tickets.html", {'tickets': tickets})

def buy_ticket(request):
    if request.method == 'GET' :
        form = TicketForm()
        route_model = Route
        bus_model = Bus
        params = {
            'form': form,
            'route_model': route_model,
            'bus_model': bus_model            
        }
    else:
        form = TicketForm(request.POST)
        params = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect("all_tickets")
    return render(request, "tickets/buy_tickets.html", params)

def edit_ticket(request, id):
    return render(request, "tickets/edit_ticket.html", {})
