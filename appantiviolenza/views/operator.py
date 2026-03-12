from django.shortcuts import render
from ..models import Ticket

def operator(request):
    tickets = Ticket.objects.all()

    return render(request, 'operator.html', {
        'tickets': tickets,
    })