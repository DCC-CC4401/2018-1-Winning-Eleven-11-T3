from django.shortcuts import render
from .models import Articulo, Usuario, Prestamo
import json

def index(request):
    total_prestamos = Prestamo.objects.all()
    reservas_list = []
    filtro_espacio = []
    if request.method == 'POST':
        for posts in request.POST:
            if "optcheck" in posts:
                filtro_espacio.append(int(request.POST[posts]))

    for prestamo in total_prestamos:
        if prestamo.id_articulo.espacio:
            if prestamo.id_articulo_id in filtro_espacio:
                reserva_dic = {
                    "title": str(prestamo.id_articulo)+"-"+str(prestamo.id_usuario),
                    "start": prestamo.fecha_inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": prestamo.fecha_termino.strftime("%Y-%m-%dT%H:%M:%S"),
                    "color": prestamo.id_articulo.color_calendario
                }
                reservas_list.append(reserva_dic)

    prestamos_filtrados=[]
    if request.method == 'POST':
        if request.POST.get('todos', False):
            for prestamos in total_prestamos:
                prestamos_filtrados.append(prestamos)
        elif request.POST.get('vigentes', False):
            for prestamos in total_prestamos:
                if prestamos.estado == "Vigente":
                    prestamos_filtrados.append(prestamos)
        elif request.POST.get('caducados', False):
            for prestamos in total_prestamos:
                if prestamos.estado == "Caducado":
                    prestamos_filtrados.append(prestamos)
        elif request.POST.get('perdidos', False):
            for prestamos in total_prestamos:
                if prestamos.estado == "Perdido":
                    prestamos_filtrados.append(prestamos)
        else:
            prestamos_filtrados=total_prestamos
    else:
        prestamos_filtrados = total_prestamos
    return render(request, 'landingAdmin/index.html', {'prestamos': Prestamo.objects.all(),
                                                       'prestamosFiltrados': prestamos_filtrados,
                                                       'articulos': Articulo.objects.all(),
                                                       'reservas': reservas_list,
                                                       'filtroEspacio': filtro_espacio})
