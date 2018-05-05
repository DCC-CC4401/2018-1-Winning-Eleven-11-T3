from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def articulos(request):
    return render(request, 'articulos.html')
