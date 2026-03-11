from django.shortcuts import render
from ..models import Utente
from ..forms import UtenteForm

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

    return render(request, 'tickets.html', {
        'fascie_eta': fascia_eta,
        'regioni_italia': REGIONI,
    })
