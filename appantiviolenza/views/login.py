from django.shortcuts import render, redirect
from ..forms import UtenteForm

def register(request):
    form = UtenteForm(request.POST or None)

    if request.method == 'POST':
        print('POST HTTP METHOD SELECTED')

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'login.html', {'registrazione': True})