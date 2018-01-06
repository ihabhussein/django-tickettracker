from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ticket, STATES
from .forms import CreateTicketForm, TicketUpdateForm, LogEntryForm


class IndexView(ListView):
    model = Ticket
    ordering = '-id'
    paginate_by = 10


class TicketView(LoginRequiredMixin, DetailView):
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TicketUpdateForm(instance=self.object)
        context['logentry_form'] = LogEntryForm()
        return context

    def post(self, request, **kwargs):
        object = Ticket.objects.get(pk=kwargs['pk'])

        form = TicketUpdateForm(request.POST)
        if form.is_valid():
            object.update(**form.cleaned_data)

        logentry_form = LogEntryForm(request.POST)
        if logentry_form.is_valid():
            print(logentry_form.cleaned_data)
            object.entries.create(created_by=request.user, **logentry_form.cleaned_data)

        return super().get(request)


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = CreateTicketForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tickettracker:detail', args=[self.object.pk])


class BoardsView(LoginRequiredMixin, TemplateView):
    template_name = 'tickettracker/boards.html'

    def get_context_data(self, **kwargs):
        kwargs['states'] = STATES
        kwargs['tickets'] = Ticket.objects.all().order_by('-id')
        return kwargs
