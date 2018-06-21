from django.shortcuts import render

from .models import Prestables, Prestamos, Solicitudes, Aforo, Profile


def index(request):
    total_solicitudes = Solicitudes.objects.all().order_by('tiempo_solicitud')
    total_prestamos = Prestamos.objects.all().order_by('id__tiempo_solicitud')
    total_espacios = Aforo.objects.all()
    reservas_list = []
    filtro_espacio = []
    colores = ['green', 'red', 'blue', 'magenta', 'cyan', 'orange']
    espacios_list = []
    i=0
    for espacio in total_espacios:
        espacio_dic = {
            "id": espacio.id.id,
            "nombre": espacio.id.nombre,
            "estado": espacio.id.estado,
            "color": colores[i],
        }
        i = i+1
        espacios_list.append(espacio_dic)

    if request.method == 'POST':
        for posts in request.POST:
            if "optcheck" in posts:
                filtro_espacio.append(int(request.POST[posts]))

        checkedPend = request.POST.getlist('checkedPend[]')
        for checked in checkedPend:
            una_solicitud = Solicitudes.objects.get(id=int(checked))
            if "aceptarPedidos" in request.POST:
                una_solicitud.estado_sol = "Aceptada"
                nuevo_prestamo = Prestamos()
                nuevo_prestamo.estado_sol = "Vigente"
                nuevo_prestamo.id = una_solicitud
                nuevo_prestamo.save()
            elif "rechazarPedidos" in request.POST:
                una_solicitud.estado_sol = "Rechazada"
            una_solicitud.save()

    for solicitud in total_solicitudes:
        if solicitud.estado_sol != 'Rechazado':
            if solicitud.id_obj_id in filtro_espacio:
                for un_espacio in espacios_list:
                    if solicitud.id_obj_id == un_espacio["id"]:
                        reserva_dic = {
                            "title": str(solicitud.id_obj)+"-"+str(solicitud.rut_per.user),
                            "start": solicitud.tiempo_inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                            "end": solicitud.tiempo_final.strftime("%Y-%m-%dT%H:%M:%S"),
                            "color": un_espacio["color"]
                        }
                        reservas_list.append(reserva_dic)

    return render(request, 'landingAdmin/index.html', {'totalPrestamos': total_prestamos,
                                                       'listaEspacios' : espacios_list,
                                                       'listaReservas': reservas_list,
                                                       'totalSolicitudes': total_solicitudes,
                                                       'filtroEspacio': filtro_espacio})
