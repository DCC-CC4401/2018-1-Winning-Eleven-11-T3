from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def articulos(request):
    return HttpResponse("Página de reserva de articulos.")
