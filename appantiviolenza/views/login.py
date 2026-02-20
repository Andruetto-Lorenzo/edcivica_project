from django.shortcuts import render, redirect
from ..forms import UtenteForm
from ..models import Utente

def register(request):
    form = UtenteForm(request.POST or None)
    regioni = ["Valle d'Aosta", "Piemonte", 
               "Liguria", "Lombardia", "Veneto", 
               "Friuli Venezia Giulia", "Trentino Alto Adige", 
               "Toscana", "Emilia Romagna", "Marche", "Umbria",
               "Abruzzo", "Lazio", "Campania", "Molise", "Puglia", "Basilicata",
               "Calabria", "Sicilia", "Sardegna"]
    
    fascia_eta = []
    for eta in Utente.FASCE_ETA_CHOICES:
        fascia_eta.append(eta[1])

    if request.method == 'POST':
        print('POST HTTP METHOD SELECTED')

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'login.html', {
        'registrazione': True,
        'regioni_italia': regioni,
        'fascie_eta': fascia_eta,
        })

def login(request):
    pass