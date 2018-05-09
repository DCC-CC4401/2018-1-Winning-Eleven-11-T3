from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo, Prestamo


def index(request):
    total_prestamos = Prestamo.objects.all().order_by('fecha_inicio')
    reservas_list = []
    filtro_espacio = []
    if request.method == 'POST':
        checkedPend = request.POST.getlist('checkedPend[]')
        for posts in request.POST:
            if "optcheck" in posts:
                filtro_espacio.append(int(request.POST[posts]))

        checkedPend = request.POST.getlist('checkedPend[]')
        for checked in checkedPend:
            un_prestamo = Prestamo.objects.get(pk=int(checked))
            if "aceptarPedidos" in request.POST:
                un_prestamo.estado = "Vigente"
            elif "rechazarPedidos" in request.POST:
                un_prestamo.estado = "Rechazado"
            un_prestamo.save()

    for prestamo in total_prestamos:
        if prestamo.id_articulo.espacio and prestamo.estado != 'Rechazado':
            if prestamo.id_articulo_id in filtro_espacio:
                reserva_dic = {
                    "title": str(prestamo.id_articulo)+"-"+str(prestamo.id_usuario),
                    "start": prestamo.fecha_inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": prestamo.fecha_termino.strftime("%Y-%m-%dT%H:%M:%S"),
                    "color": prestamo.id_articulo.color_calendario
                }
                reservas_list.append(reserva_dic)

    return render(request, 'landingAdmin/index.html', {'prestamos': total_prestamos,
                                                       'articulos': Articulo.objects.all(),
                                                       'reservas': reservas_list,
                                                       'filtroEspacio': filtro_espacio})
