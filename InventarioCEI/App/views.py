from django.shortcuts import render
from .models import Articulo


# Create your views here.
def busqueda_simple(request):
    context = {}
    if request.method == 'POST':
        busqueda = Articulo.objects.all()
        if request.POST.get('nombre', False):
            busqueda = busqueda.filter(nombre=request.POST['nombre'])
            context['busqueda'] = busqueda[:12]
    populares = Articulo.objects.all().order_by("-solicitudes")[:6]
    context['populares'] = populares
    return render(request, 'articulos-bsimple.html', context)


def busqueda_avanzada(request):
    context = {}
    if request.method == 'POST':
        busqueda = Articulo.objects.all()
        if request.POST.get('nombre', False):
            busqueda = busqueda.filter(nombre=request.POST['nombre'])
            context['busqueda'] = busqueda[:12]
        if request.POST.get('estado', False):
            if request.POST['estado'] == 'any':
                context['busqueda'] = busqueda[:12]
            else:
                busqueda = busqueda.filter(estado=request.POST['estado'])
                context['busqueda'] = busqueda[:12]
    populares = Articulo.objects.all().order_by("-solicitudes")[:6]
    context['populares'] = populares
    return render(request, 'articulos-bavanzada.html', context)
