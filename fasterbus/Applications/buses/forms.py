from django import forms
from .models import Bus

class BusForm( forms.ModelForm ):
    class Meta:
        model = Bus
        fields = ('plate', 'type', 'capacity', 'company')
        widgets = {
            'plate': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Placa',
                'pattern': '[A-Z]{3}-[0-9]{3}'
                }),
            'type': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Tipo'
                }),
            'capacity': forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Capacidad'
                }),
            'company': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Empresa'
                })            
        }