from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from ..forms import UtenteForm
from ..models import Utente

def register_view(request):
    mode = request.GET.get("mode", "register")
    print(mode)
    registrazione = (mode == "register")
    print(registrazione)

    form = UtenteForm(request.POST or None)

    if request.method == 'POST':
        print('POST HTTP METHOD SELECTED')

        if form.is_valid():
            form.save()
        username = request.POST.get("username")
        print("username scelto: ", username)

        nome_utente = request.POST.get("nome_utente")
        passw = request.POST.get("password")
        user = authenticate(request, username=nome_utente, password=passw)
        
        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            print('login non valido.')

    return render(request, 'login.html')
