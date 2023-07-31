from django import forms
from django.forms import DateInput
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'name', 'customer_email', 'date', 'time', 'end_time', 'notes', 'table', 'number_of_guests']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }