from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        print('POST HTTP METHOD SELECTED')
    return render(request, 'login.html', {'registrazione': True})