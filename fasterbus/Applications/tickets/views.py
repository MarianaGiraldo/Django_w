from django.shortcuts import render, redirect

from Applications.routes.models import Route
from Applications.buses.models import Bus
from .models import Ticket
from .forms import TicketForm

def all_tickets(request):
    tickets = Ticket.objects.all()
    route_model = Route
    bus_model = Bus
    print(tickets[0].route)
    return render(request, "tickets/all_tickets.html", {
        'tickets': tickets,
        'route_model': route_model,
        'bus_model': bus_model 
    })

def buy_ticket(request):
    title = "Comprar tiquete"
    if request.method == 'GET' :
        form = TicketForm()
        params = {
            'form': form,
            'title': title           
        }
    else:
        form = TicketForm(request.POST)
        params = {
            'form': form,
            'title': title 
        }
        if form.is_valid():
            form.save()
            return redirect("all_tickets")
    return render(request, "tickets/buy_tickets.html", params)

def edit_ticket(request, id):
    title = "Editar tiquete"
    ticket = Ticket.objects.get( id = id )
    if request.method == 'GET' :
        form = TicketForm( instance = ticket )
    else:
        form = TicketForm(request.POST,  instance = ticket )
        if form.is_valid():
            form.save()
            return redirect("all_tickets")
    return render(request, "tickets/buy_tickets.html", {'form': form, 'title': title })

def delete_ticket(request, id):
    ticket = Ticket.objects.get( id = id )
    ticket.delete()
    return redirect("all_tickets")
