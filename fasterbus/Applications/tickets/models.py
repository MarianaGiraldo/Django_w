from django.db import models
from Applications.routes.models import Route
from Applications.buses.models import Bus
from Applications.passengers.models import Passenger

class Ticket(models.Model):
    id = models.AutoField(primary_key = True)
    route = models.ForeignKey( Route, on_delete=models.CASCADE)
    bus = models.ForeignKey( Bus, on_delete=models.CASCADE)
    passenger = models.ForeignKey( Passenger, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    travel_date = models.DateField()
    departure_time = models.TimeField()
    
    
