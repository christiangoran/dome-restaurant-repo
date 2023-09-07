from django import forms
from django.forms import DateInput
from .models import Reservation, BOOKING_TIME, Table
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import datetime


class ReservationForm(forms.ModelForm):
    """
    A  ModelForm for handling table reservations.

    Attributes:
        time (ChoiceField): A choice field for selecting the booking time.
        Meta: Meta class for specifying model and fields.

    Methods:
        clean: Custom validation for the form.

    In the form the folowing fields are included:
        - name: The name of the person making the reservation. *required*
        - customer_email: The email address of the customer.
        - date: The date of the reservation. *required*
        - time: The time of the reservation. *required*
        - notes: Additional notes or special requests.
        - number_of_guests: The number of guests for the reservation. *required*

    The form also performs custom validation to check:
        - If the selected date is in the future.
        - If there are tables available for the selected date and time.
        - If there are tables with sufficient capacity for the number of guests.
    """
    
    time = forms.ChoiceField(choices=BOOKING_TIME, widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Reservation
        fields = [
            'name', 'customer_email', 'date', 'time',
            'notes', 'number_of_guests'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'date': DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'notes': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'number_of_guests': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                    'min': 1,
                    'max': 8
                }
            ),
        }

    def clean(self):

        date = self.cleaned_data.get('date', None)
        time = self.cleaned_data.get('time', None)
        guests = self.cleaned_data.get('number_of_guests', None)

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
        new_tables_with_capacity = []
        for table in tables_with_capacity:
            is_table_booked = any(
                table.table_number == booking.table.table_number
                for booking in bookings_on_requested_date
            )
            if not is_table_booked:
                new_tables_with_capacity.append(table)

        tables_with_capacity = new_tables_with_capacity

        # add booked table to list of tables with capacity
        if table_booked is not None:
            if table_booked.capacity >= guests and not any(
                    booking.table.table_number == table_booked.table_number
                    for booking in bookings_on_requested_date):
                tables_with_capacity.append(table_booked)

        # throw validation errors on form
        if date < datetime.date.today():
            raise ValidationError('Sorry you have to book a future date')

        if bookings_on_requested_date.count() >= 5:
            raise ValidationError(
                'Sorry we do not have a table'
                ' available for that date and time'
            )

        if not tables_with_capacity:
            raise ValidationError(
                'Sorry we do not have a table with that capacity available')


class SearchReservationForm(forms.Form):
    """
    This form is for searching existing table reservations.
    Available in staff accounts only.

    Attributes:
        booking_email (EmailField): An email field for searching by booking email.
        booking_date (DateField): A date field for searching by booking date.

    The form includes these fields:
        - booking_email: The email address used for the reservation.
        - booking_date: The date of the reservation.

    Both fields are optional and can be used to filter reservations based on either or both criteria.

    The form uses custom widgets with specific attributes for better user experience:
        - 'autocomplete': turned off for both fields.
        - 'aria-label': for accessibility.
        - 'placeholder': to guide the user.
        - 'class': for styling.
    """
    booking_email = forms.EmailField(
        label='Search Booking Email',
        required=False,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'off',
                'aria-label': 'Search Booking by Email',
                'placeholder': 'Search Booking Email',
                'class': 'form-control'
            }))
    booking_date = forms.DateField(
        label='Search Booking Date',
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'autocomplete': 'off',
                'aria-label': 'Search Bookings by date',
                'placeholder': 'Search Booking Date',
                }))
