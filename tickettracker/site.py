from django.urls import path

from .views import IndexView, TicketView, TicketCreateView, BoardsView


urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('tickets/<int:pk>', TicketView.as_view(), name='detail'),
    path('create', TicketCreateView.as_view(), name='create'),
    path('boards', BoardsView.as_view(), name='boards'),
]

def get_urls():
    return urlpatterns, 'tickettracker', 'tickettracker'

urls = get_urls()
