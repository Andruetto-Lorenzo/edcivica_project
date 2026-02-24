from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ..forms import UtenteForm
from ..models import Utente

def register(request):
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
        print('POST HTTP METHOD SELECTED')

        if form.is_valid():
            form.save()
        username = request.POST.get("username")
        print("username scelto: ", username)

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        telefono = request.POST.get("telefono")
        eta_scelta = request.POST.get("fascia_eta")
        regione = request.POST.get("regione_provenienza")

        utente = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        Utente.objects.create(
            nome_utente=username,
            email=email,
            password=utente.password,
            telefono=telefono,
            fascia_eta=eta_scelta,
            regione_provenienza=regione,
        )

        print(utente.username, utente.email, utente.password)

        return redirect('home')
    # if request.method == 'GET':
    #     print("GET HTTP METHOD SELECTED")

        # utente = Utente.objects.create_user(
        #     username="",
        #     password="",
        # )


    return render(request, 'login.html', {
        'registrazione': True,
        'regioni_italia': REGIONI,
        'fascie_eta': fascia_eta,
        })

def login(request):
    return render(request, 'login.hmtl', {
        'registrazione': False,
    })