from django.shortcuts import render
from ..models import Ticket

def operator_view(request):
    tickets = Ticket.objects.all()

    return render(request, 'operator.html', {
        'tickets': tickets,
    })