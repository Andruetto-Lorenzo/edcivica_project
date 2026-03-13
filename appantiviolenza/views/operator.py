from django.shortcuts import render
from ..models import Ticket

def operator_view(request):
    tickets = Ticket.objects.all()
    # ticket.stato_richiesta = "In carico"
    # ticket.save()

    if request.method == 'POST':
        btn_accetta = request.POST.get("btn_accetta")
        if btn_accetta == 'Aperta':
            btn_accetta = 'In carico'
        else:
            btn_accetta = 'Chiusa'

        print(btn_accetta)

    print(tickets[0].stato_richiesta)

    return render(request, 'operator.html', {
        'tickets': tickets,
    })

def change_state_tickets(request):
    ticket = request.POST.get("btn_accetta")
    print(ticket)