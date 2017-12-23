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
    list_display = ('id', 'created_at', 'created_by', 'subject', 'state',)
    ordering = ('-id',)
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
