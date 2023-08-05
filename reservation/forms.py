from django import forms
from django.forms import DateInput
from .models import Reservation, BOOKING_TIME, Table
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import datetime

class ReservationForm(forms.ModelForm):
    time = forms.ChoiceField(choices=BOOKING_TIME, widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Reservation
        fields = ['name', 'customer_email', 'date', 'time',
                  'notes', 'number_of_guests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'number_of_guests': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'min': 1, 'max': 12}),

        }

    def clean(self):

        date = self.cleaned_data['date']
        time = self.cleaned_data['time']
        guests = self.cleaned_data['number_of_guests']
    
        table_booked = None
    
        try:
            table_booked = Table.objects.get(id=self.instance.table.id)
        except ObjectDoesNotExist:
            pass
    
        # Filter tables with capacity greater or equal
        # to the number of guests
        tables_with_capacity = list(Table.objects.filter(
            capacity__gte=guests
        ))
    
        # Get bookings on specified date
        bookings_on_requested_date = Reservation.objects.filter(
            date=date, time=time)
    
        # Iterate over bookings to get tables not booked
        for booking in bookings_on_requested_date:
            for table in tables_with_capacity:
                if table.table_number == booking.table.table_number:
                    tables_with_capacity.remove(table)
                    break

        #add booked table to list of tables with capacity
        if table_booked is not None:
            if table_booked.capacity >= guests and not any(
                booking.table.table_number == table_booked.table_number 
                for booking in bookings_on_requested_date):
                tables_with_capacity.append(table_booked)   

        #throw validation errors on form
        if date < datetime.date.today():
            raise ValidationError('Sorry you have to book a future date')
        
        if table_booked is not None:
            if table_booked.capacity < guests:
                raise ValidationError('Sorry we do not have a table with that capacity available')

        if not tables_with_capacity:
            raise ValidationError('Sorry we do not have a table available for that date and time')      
        

class SearchReservationForm(forms.Form):
    booking_email = forms.EmailField(label='Search Booking Email', required=False, widget=forms.TextInput(
        attrs={
            'autocomplete': 'off', 
            'aria-label': 'Search Booking by Email', 
            'placeholder': 'Search Booking Email',
            'class': 'form-control'
            }))
    booking_date = forms.DateField(label='Search Booking Date', required=False, widget=forms.DateInput(
        attrs={
            'class': 'form-control', 
            'type': 'date',
            'autocomplete': 'off', 
            'aria-label': 'Search Bookings by date', 
            'placeholder': 'Search Booking Date',
            }))
