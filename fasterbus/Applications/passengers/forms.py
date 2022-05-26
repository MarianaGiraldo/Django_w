from django import forms
from .models import Passenger

class PassengerForm( forms.ModelForm ):
    class Meta:
        model = Passenger
        fields = ('full_name', 'document', 'email', 'phone', 'password')
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nombre completo'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'placeholder': 'Correo electrónico'
                }),
            'phone': forms.TextInput(attrs={
                'class': "form-control", 
                'type': "tel",
                'placeholder': 'Teléfono'
                }),
            'document': forms.TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Cedula'
                }),
            'password': forms.PasswordInput(attrs={
                'class': "form-control", 
                'placeholder': 'Contraseña'
                })
            
        }