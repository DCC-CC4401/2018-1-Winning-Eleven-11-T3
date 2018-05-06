from django.shortcuts import render
from .models import Articulo, Usuario, Prestamo


def index(request):
    return render(request, 'landingAdmin/index.html', {'prestamos': Prestamo.objects.all() ,
                                                       'articulos': Articulo.objects.all()})