from django.urls import path
import Applications.tickets.views as t

urlpatterns = [
    path('all-tickets', t.all_tickets, name="all_tickets"),
    path('buy-tickets', t.buy_ticket, name="insert_ticket"),
    path('tickets/edit/<int:id>', t.edit_ticket, name="edit_ticket")
]