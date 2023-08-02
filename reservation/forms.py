from django import forms
from django.forms import DateInput
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'customer_email', 'date', 'time', 'end_time', 'notes', 'table', 'number_of_guests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'time': DateInput(attrs={'class': 'form-control'}),
            'end_time': DateInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
            'table': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_guests': forms.TextInput(attrs={'class': 'form-control'}) ,
            
        }