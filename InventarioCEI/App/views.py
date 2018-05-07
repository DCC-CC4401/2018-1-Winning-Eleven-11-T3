from django.shortcuts import render
from .models import Articulo


# Create your views here.
def buscar_articulos(request):
    context = {
        'modo': 'basico',
    }
    if request.method == 'POST':
        if request.POST.get('modo', False) == "1":
            context['modo'] = 'avanzado'
        else:
            context['modo'] = 'basico'
        busqueda = Articulo.objects
        if request.POST.get('nombre', False):
            busqueda = busqueda.filter(nombre=request.POST['nombre'])
            context['busqueda'] = busqueda
        if request.POST.get('estado', False):
            if request.POST['estado'] != 'any':
                busqueda = busqueda.filter(nombre=request.POST['estado'])
                context['busqueda'] = busqueda
    populares = Articulo.objects.all().order_by("-solicitudes")[:5]
    context['populares'] = populares
    return render(request, 'articulos.html', context)
