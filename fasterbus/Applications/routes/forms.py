from django import forms
from .models import Route

class RouteForm( forms.ModelForm ):
    class Meta:
        model = Route
        fields = ('origin', 'destination')
        widgets = {
            'origin': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Origen'
                }),
            'destination': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Destino'
                })     
        }