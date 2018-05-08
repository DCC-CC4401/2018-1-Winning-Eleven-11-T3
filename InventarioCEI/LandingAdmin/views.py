from django.shortcuts import render
from .models import Articulo, Usuario, Prestamo, Reserva, Espacio
import json

def index(request):
    reservas = Reserva.objects.all()
    espacios = Espacio.objects.all()
    reservas_list = []
    filtroEspacio = []
    if request.method == 'POST':
        for posts in request.POST:
            if "optcheck" in posts:
                filtroEspacio.append(int(request.POST[posts]))

    for res in reservas:
        if res.id_espacio_id in filtroEspacio:
            reserva_dic = {
                "title": str(res.id_espacio)+"-"+str(res.id_usuario),
                "start": res.fecha_inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                "end": res.fecha_termino.strftime("%Y-%m-%dT%H:%M:%S"),
                "color": res.id_espacio.color_calendario
            }
            reservas_list.append(reserva_dic)

    return render(request, 'landingAdmin/index.html', {'prestamos': Prestamo.objects.all(),
                                                       'articulos': Articulo.objects.all(),
                                                       'reservas': reservas_list,
                                                       'espacios': Espacio.objects.all(),
                                                        'filtroEspacio': filtroEspacio})
