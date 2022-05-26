from django import forms
from .models import Bus

class BusForm( forms.ModelForm ):
    class Meta:
        model = Bus
        fields = ('plate', 'type', 'capacity', 'company')