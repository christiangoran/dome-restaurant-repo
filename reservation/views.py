from typing import Any, Dict
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic
from .forms import ReservationForm, SearchReservationForm
from .models import Reservation, Table
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.contrib import messages
import datetime


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'home'
        return context


class MenuView(generic.TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'menu'
        return context


class InformationView(generic.TemplateView):
    template_name = 'information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'information'
        return context


class IndexReservation(LoginRequiredMixin, ListView):
    """
    I've used a lot of my mentors Gareth McGirr's code for this view with some
    modifications to suit my project. His code can be found here:
    https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak
    """
    template_name = 'view_reservations.html'
    login_url = '/accounts/login'  # If user not logged in, redirect > /login
    context_object_name = 'reservations'
    model = Reservation

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = super().get_queryset()
            booking_email = self.request.GET.get('booking_email')
            booking_date = self.request.GET.get('booking_date')

            if booking_email:  # If booking_email is not None
                queryset = queryset.filter(customer_email=booking_email)

            if booking_date:
                queryset = queryset.filter(date=booking_date)

            queryset = queryset.filter(
                date__gte=datetime.date.today()-datetime.timedelta(days=1))

            # If user is staff, return all reservations from today onwards
            return queryset

        else:
            # If user is not staff, return only reservations made by user
            return Reservation.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchReservationForm(
            self .request.GET or None)
        context['navbar'] = 'view'
        return context


class CreateReservation(generic.edit.CreateView):
    """
    A class based view for creating a reservation.

    Attributes:
    - template_name: The template used for the view.
    - model: The model used for the view.
    - form_class: The form used for the view.
    - success_url: The url to redirect to after a successful form submission.

    Methods:
    - form_valid: This method is called when valid form data has been POSTed.
    
    I've used a lot of my mentors Gareth McGirr's code for this class with some
    modifications to suit my project. His code can be found here:
    https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak

    """
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
        """
        This method returns the object that the view will display.
        """
        reservation = super().get_object(queryset=queryset)
        if self.request.user.is_staff or self.request.user == reservation.user:
            return reservation
        else:
            raise Http404("You are not authorized to edit this reservation.")

    def form_valid(self, form):
        """
        After the form is submitted, this wills end a success message with info
        """
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        guests = form.cleaned_data['number_of_guests']

        messages.success(
            self.request,
            f'Booking updated for {guests} guests on {date} at '
            f'{form.instance.get_time_display()}'
        )

        return super(UpdateReservation, self).form_valid(form)


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
            raise Http403("You are not authorized to edit this reservation.")

    def delete(self, request, *args, **kwargs):
        """
        After the reservation is deleted, this will show a notification
        """
        reservation = self.get_object()
        messages.success(
            self.request,
            f'Booking cancelled for {reservation.number_of_guests} '
            f'guests on {reservation.date} at {reservation.get_time_display()}'
        )
        return super().delete(request, *args, **kwargs)


class CustomLoginView(LoginView):
    """
    This view is created to get active navbar link
    """
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'login'  # This is used to get active navbar link
        return context


def SignupView(request):
    context = {
        'signup_url': reverse('reservation:signup')
    }
    return render(request, 'account/signup.html', context)
