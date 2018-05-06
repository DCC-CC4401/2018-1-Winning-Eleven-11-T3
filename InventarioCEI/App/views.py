from django.shortcuts import render
from .models import Articulo


# Create your views here.
def buscar_articulos(request):
    populares = Articulo.objects.all().order_by("-solicitudes")[:5]
    context = {
        'populares': populares,
    }
    return render(request, 'articulos.html', context)
