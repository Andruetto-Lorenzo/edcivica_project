from django.shortcuts import render, redirect
from ..forms import UtenteForm

def register(request):
    form = UtenteForm(request.POST or None)
    regioni = ["Valle d'Aosta", "Piemonte", 
               "Liguria", "Lombardia", "Veneto", 
               "Friuli Venezia Giulia", "Trentino Alto Adige", 
               "Toscana", "Emilia Romagna", "Marche", "Umbria",
               "Abruzzo", "Lazio", "Campania", "Molise", "Puglia", "Basilicata",
               "Calabria", "Sicilia", "Sardegna"]

    if request.method == 'POST':
        print('POST HTTP METHOD SELECTED')

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'login.html', {
        'registrazione': True,
        'regioni_italia': regioni,
        })

def login(request):
    pass