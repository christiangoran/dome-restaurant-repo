from django import forms
from django.forms import DateInput
from .models import Reservation, BOOKING_TIME


class ReservationForm(forms.ModelForm):
    time = forms.ChoiceField(choices=BOOKING_TIME, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Reservation
        fields = ['name', 'customer_email', 'date', 'time',
                  'notes', 'table', 'number_of_guests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': DateInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'table': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_guests': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'min': 1, 'max': 12}),

        }
