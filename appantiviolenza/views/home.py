from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# from django.http import HttpResponse, HttpResponseNotFound
# from django.shortcuts import render, redirect, get_object_or_404
# from . import models as m