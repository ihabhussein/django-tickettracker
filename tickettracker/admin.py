from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# from .forms import QueueForm, EmployeeForm, AdvertForm
from .models import Product, Milestone, Ticket


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    ordering = ('label',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    ordering = ('-id',)
