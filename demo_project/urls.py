from django.contrib import admin
from django.urls import path

import tickettracker.site as tickettracker


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tickettracker.urls),
]
