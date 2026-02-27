from django.shortcuts import render, redirect

def operator(request):
    return render(request, 'operator.html', {
        'name': 'marco',
    })