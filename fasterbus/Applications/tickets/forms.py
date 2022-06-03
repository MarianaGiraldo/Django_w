from django import forms
from .models import Ticket

class TicketForm( forms.ModelForm ):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            'route_id': forms.Select(attrs={
                'class': "form-control py-0 px-2",
                'placeholder': 'Seleccione su ruta'
                }),
            'bus_id': forms.Select(attrs={
                'class': "form-control py-0 px-2",
                'placeholder': 'Seleccione el bus'
                }),
            'passenger_id': forms.Select(attrs={
                'class': "form-control py-0 px-2",
                'placeholder': 'Seleccione el usuario'
                }),
            'travel_date': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Fecha de viaje',
                'onfocus' : "(this.type='date')",
                'onblur' : "(this.type='text')"
                }),
            'departure_time': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Hora de salida',
                'onfocus' : "(this.type='time')"
                })  ,
            'quantity': forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Cantidad',
                'min' : "1"
                })
        }