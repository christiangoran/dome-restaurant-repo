from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Reservation, Table

class IndexReservation(generic.ListView):
    template_name = 'reservations/index.html'
    context_object_name = 'latest_reservation_list'

    def get_queryset(self):
        return Reservation.objects.filter(date__lte=timezone.now()).order_by('-date')

class DetailReservation(generic.DetailView):
    model = Reservation
    template_name = 'reservations/detail.html'

class CreateReservation(generic.edit.CreateView):
    model = Reservation
    fields = ['user', 'date', 'start_time', 'end_time', 'notes', 'table', 'number_of_guests', 'image']
    template_name = 'reservations/create.html'

class UpdateReservation(generic.edit.UpdateView):
    model = Reservation
    fields = ['user', 'date', 'start_time', 'end_time', 'notes', 'table', 'number_of_guests', 'image']
    template_name = 'reservations/update.html'

class DeleteReservation(generic.edit.DeleteView):
    model = Reservation
    success_url = reverse_lazy('reservations:index')
    template_name = 'reservations/delete.html'