from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class IndexReservation(LoginRequiredMixin, ListView):
    template_name = 'view_reservations.html'
    login_url = '/accounts/login'  # If user is not logged in, redirect to /login/
    context_object_name = 'reservations'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                # This is a staff user, show all reservations
                return Reservation.objects.all().order_by('date', 'time')
            else:
                # This is a regular user, show only their reservations
                return Reservation.objects.filter(user=self.request.user).order_by('date')


class CreateReservation(generic.edit.CreateView):
    template_name = 'create_reservation.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservation:home')

    def form_valid(self, form):
        """This method is called when valid form data has been POSTed.
        and ensures that the user creating the reservation is attached to the reservation.
        record before saving it."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateReservation(generic.edit.UpdateView):
    template_name = 'update_reservation.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('reservation:home')

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
    success_url = reverse_lazy('reservation:home')

    def get_object(self, queryset=None):
        """This method returns the object that the view will display."""
        reservation = super().get_object(queryset=queryset)
        if self.request.user.is_staff or self.request.user == reservation.user:
            return reservation
        else:
            raise Http404("You are not authorized to edit this reservation.")
