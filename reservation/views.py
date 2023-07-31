from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from .forms import ReservationForm
from .models import Reservation, Table

from .models import Reservation, Table

class IndexReservation(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_reservation_list'

    def get_queryset(self):
        return Reservation.objects.all().order_by('-date')

class DetailReservation(generic.DetailView):
    model = Reservation
    template_name = 'detail.html'

class CreateReservation(generic.edit.CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'create_reservation.html'
    success_url = reverse_lazy('reservation:home')

class UpdateReservation(generic.edit.UpdateView):
    model = Reservation
    fields = ['user', 'date', 'start_time', 'end_time', 'notes', 'table', 'number_of_guests', 'image']
    template_name = 'update_reservation.html'

class DeleteReservation(generic.edit.DeleteView):
    model = Reservation
    success_url = reverse_lazy('reservations:index')
    template_name = 'delete_reservation.html'