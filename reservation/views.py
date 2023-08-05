from typing import Any, Dict
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic
from .forms import ReservationForm, SearchReservationForm
from .models import Reservation, Table
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.contrib import messages


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class IndexReservation(LoginRequiredMixin, ListView):
    template_name = 'view_reservations.html'
    login_url = '/accounts/login'  # If user is not logged in, redirect to /login/
    context_object_name = 'reservations'
    model = Reservation

    def get_queryset(self):
        queryset = super().get_queryset()
        booking_email = self.request.GET.get('booking_email')
        booking_date = self.request.GET.get('booking_date')

        if booking_email:  # If booking_email is not None
            queryset = queryset.filter(customer_email=booking_email)

        if booking_date:
            queryset = queryset.filter(date=booking_date)

        return queryset    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['search_form'] = SearchReservationForm(self .request.GET or None)
        return context



class CreateReservation(generic.edit.CreateView):
    template_name = 'create_reservation.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservation:view') 

    def form_valid(self, form):
        """
        Before form submission, assign table with lowest capacity
        needed for booking guests
        """
        form.instance.user = self.request.user
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        guests = form.cleaned_data['number_of_guests']
        # Filter tables with capacity greater or equal
        # to the number of guests
        # *__gte is a Django query filter that means greater than or equal to
        tables_with_capacity = list(Table.objects.filter(
            capacity__gte=guests
        ))
        # Get bookings on specified date
        bookings_on_requested_date = Reservation.objects.filter(
            date=date, time=time)
        # ----Variables created for testing purposes----
        # Iterate over bookings to get tables not booked
        for booking in bookings_on_requested_date:
            for table in tables_with_capacity:
                if table.table_number == booking.table.table_number:
                    tables_with_capacity.remove(table)
                    break
        # Iterate over tables not booked to get lowest
        # capacity table to assign to booking
        lowest_capacity_table = tables_with_capacity[0]
        for table in tables_with_capacity:
            if table.capacity < lowest_capacity_table.capacity:
                lowest_capacity_table = table
        form.instance.table = lowest_capacity_table

        messages.success(
            self.request,
            f'Booking confirmed for {guests} guests on {date}'
        )

        return super(CreateReservation, self).form_valid(form)


class UpdateReservation(generic.edit.UpdateView):
    template_name = 'update_reservation.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservation:view')

    def get_object(self, queryset=None):
        """This method returns the object that the view will display."""
        reservation = super().get_object(queryset=queryset)
        if self.request.user.is_staff or self.request.user == reservation.user:
            return reservation
        else:
            raise Http404("You are not authorized to edit this reservation.")


class DeleteReservation(generic.edit.DeleteView):
    template_name = 'delete_reservation.html'
    model = Reservation
    success_url = reverse_lazy('reservation:view')

    def get_object(self, queryset=None):
        """This method returns the object that the view will display."""
        reservation = super().get_object(queryset=queryset)
        if self.request.user.is_staff or self.request.user == reservation.user:
            return reservation
        else:
            raise Http404("You are not authorized to edit this reservation.")
