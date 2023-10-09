from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "Regioes/index.html")

def norte(request):
    return render(request, "Regioes/norte.html")

def nordeste(request):
    return render(request, "Regioes/nordeste.html")