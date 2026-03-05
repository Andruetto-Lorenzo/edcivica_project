from django.shortcuts import render

def tickets(request):
    render(request, 'tickets.html')