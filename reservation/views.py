from django.shortcuts import render, get_object_or_404
from django.http import  Http404
from django.urls import  reverse_lazy
from django.views import generic
from django.utils import timezone
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

class HomeView(generic.TemplateView):
    template_name = 'index.html'
    context_object_name = 'reservations'

class IndexReservation(LoginRequiredMixin, ListView):
    login_url = '/accounts/login' # If user is not logged in, redirect to /login/
    template_name = 'view_reservations.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                # This is a staff user, show all reservations
                return Reservation.objects.all().order_by('date')
            else:
                # This is a regular user, show only their reservations
                return Reservation.objects.filter(user=self.request.user).order_by('date')
        else:
            # This is an anonymous user, show no reservations
            return Reservation.objects.none()
        

            

class CreateReservation(generic.edit.CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'create_reservation.html'
    success_url = reverse_lazy('reservation:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateReservation(generic.edit.UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'update_reservation.html'
    success_url = reverse_lazy('reservation:home')

    def get_object(self, queryset=None):
        """This method returns the object that the view will display."""
        reservation = super().get_object(queryset=queryset)
        if self.request.user.is_staff or self.request.user == reservation.user:
            return reservation
        else:
            raise Http404("You are not authorized to edit this reservation.")

class DeleteReservation(generic.edit.DeleteView):
    model = Reservation
    template_name = 'delete_reservation.html'
    success_url = reverse_lazy('reservation:home')

    def get_object(self, queryset=None):
        """This method returns the object that the view will display."""
        reservation = super().get_object(queryset=queryset)
        if self.request.user.is_staff or self.request.user == reservation.user:
            return reservation
        else:
            raise Http404("You are not authorized to edit this reservation.")