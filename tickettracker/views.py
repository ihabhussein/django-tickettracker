from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView

from .models import Ticket
from .forms import CreateTicketForm


class IndexView(ListView):
    model = Ticket
    ordering = '-id'
    paginate_by = 10


class TicketView(DetailView):
    model = Ticket


class TicketCreateView(CreateView):
    model = Ticket
    form_class = CreateTicketForm

    def get_success_url(self):
        return reverse('tickettracker:detail', args=[self.object.pk])
