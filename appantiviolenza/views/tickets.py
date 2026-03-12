from django.shortcuts import render
from ..models import Utente
from ..forms import UtenteForm
from ..models import Ticket

def tickets(request):
    form = UtenteForm(request.POST or None)
    REGIONI = ["Valle d'Aosta", "Piemonte", 
                "Liguria", "Lombardia", "Veneto", 
                "Friuli Venezia Giulia", "Trentino Alto Adige", 
                "Toscana", "Emilia Romagna", "Marche", "Umbria",
                "Abruzzo", "Lazio", "Campania", "Molise", "Puglia", "Basilicata",
                "Calabria", "Sicilia", "Sardegna"]
    fascia_eta = []

    for eta in Utente.FASCE_ETA_CHOICES:
        fascia_eta.append(eta[1])

    if request.method == 'POST':
        print("ticket inviato")

        utente = {
            'nome': request.POST.get("username"),
            'email': request.POST.get("email"),
            'telefono': request.POST.get("telefono"),
            'eta': request.POST.get("fascia_eta"),
            'regione': request.POST.get("regione_provenienza"),
        }

        ticket = {
            'data': request.POST.get("data"),
            'ora': request.POST.get("ora"),
            'tipo_violenza': request.POST.get("tipo_violenza"),
            'descrizione': request.POST.get("descrizione"),
            'livello_urgenza': request.POST.get("importanza"),
            'stato_richiesta': request.POST.get("stato_richiesta"),
        }

        Utente.objects.create(
            nome_utente=utente['nome_utente'],
            email=utente['email'],
            
        )

        Ticket.objects.create(
            data=ticket['data'],
            ora=ticket['ora'],
            tipo_violenza=ticket['tipo_violenza'],
            descrizione=ticket['descrizione'],
            livello_urgenza=ticket['livello_urgenza'],
            stato_richiesta=ticket['stato_richiesta']
        )

    return render(request, 'tickets.html', {
        'fascie_eta': fascia_eta,
        'regioni_italia': REGIONI,
    })
