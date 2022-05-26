from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/all_tickets.html", {'tickets': tickets})

def buy_ticket(request):
    if request.method == 'GET' :
        form = TicketForm()
    else:
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_tickets")
    return render(request, "tickets/buy_tickets.html", { 'form': form })

def edit_ticket(request, id):
    return render(request, "tickets/edit_ticket.html", {})
