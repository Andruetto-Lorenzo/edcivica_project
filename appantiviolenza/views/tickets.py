from django.shortcuts import render
from ..models import Ticket

def tickets_view(request):
    REGIONI = ["Valle d'Aosta", "Piemonte", 
                "Liguria", "Lombardia", "Veneto", 
                "Friuli Venezia Giulia", "Trentino Alto Adige", 
                "Toscana", "Emilia Romagna", "Marche", "Umbria",
                "Abruzzo", "Lazio", "Campania", "Molise", "Puglia", "Basilicata",
                "Calabria", "Sicilia", "Sardegna"]
    fascia_eta = []
    tipi_violenza = []
    livello_urgenza = []

    for eta in Ticket.FASCE_ETA_CHOICES:
        fascia_eta.append(eta[1])

    for violenza in Ticket.VIOLENZA_CHOICES:
        tipi_violenza.append(violenza[1])

    for livello in Ticket.LIVELLO_URGENZA_CHOICES:
        livello_urgenza.append(livello[1])

    if request.method == 'POST':
        print("ticket inviato")
 
        ticket = {
            'nome': request.POST.get("username"),
            'email': request.POST.get("email"),
            'telefono': int(request.POST.get("telefono")),
            'eta': request.POST.get("fascia_eta"),
            'regione': request.POST.get("regione_provenienza"),
            'tipo_violenza': request.POST.get("tipo_violenza"),
            'descrizione': request.POST.get("descrizione"),
            'livello_urgenza': request.POST.get("importanza"),
            'stato_richiesta': 'Aperta',
        }

        Ticket.objects.create(
            nome_utente=ticket['nome'],
            email=ticket['email'],
            telefono=ticket['telefono'],
            fascia_eta=ticket['eta'],
            regione_provenienza=ticket['regione'],
            tipo_violenza=ticket['tipo_violenza'],
            descrizione=ticket['descrizione'],
            livello_urgenza=ticket['livello_urgenza'],
            stato_richiesta=ticket['stato_richiesta']
        )

    return render(request, 'tickets.html', {
        'fascie_eta': fascia_eta,
        'regioni_italia': REGIONI,
        'tipo_violenza': tipi_violenza,
        'livello_urgenza': livello_urgenza,
        'stato_richiesta': Ticket.stato_richiesta,
    })
