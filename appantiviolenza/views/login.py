from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register_view(request):
    if request.method == 'POST':
        print('POST HTTP METHOD SELECTED')

        username = request.POST.get("username")
        print("username scelto: ", username)

        passw = request.POST.get("password")
        user = authenticate(request, username=username, password=passw)
        
        if user is not None:
            login(request, user)
            print('login eseguito con successo')
            return redirect('operator_space')
        else:
            print('login non valido.')

    return render(request, 'login.html')
