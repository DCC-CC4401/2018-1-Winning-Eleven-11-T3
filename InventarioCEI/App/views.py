from django.shortcuts import render
from .models import Prestables
from django.http import JsonResponse
import os
from datetime import datetime
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from userSystem.models import Usuarios
from App.models import Solicitudes, Prestamos


# Create your views here.
def busqueda_simple(request):
    context = {}
    if request.method == 'POST':
        busqueda = Prestables.objects.all()
        if request.POST.get('nombre', False):
            busqueda = busqueda.filter(nombre=request.POST['nombre'])
            context['busqueda'] = busqueda[:12]
    populares = Prestables.objects.all().order_by("-solicitudes")[:6]
    context['populares'] = populares
    return render(request, 'articulos/articulos-bsimple.html', context)


def busqueda_avanzada(request):
    context = {}
    if request.method == 'POST':
        busqueda = Prestables.objects.all()
        if request.POST.get('nombre', False):
            busqueda = busqueda.filter(nombre=request.POST['nombre'])
            context['busqueda'] = busqueda[:12]
        if request.POST.get('estado', False):
            if request.POST['estado'] == 'any':
                context['busqueda'] = busqueda[:12]
            else:
                busqueda = busqueda.filter(estado=request.POST['estado'])
                context['busqueda'] = busqueda[:12]
    populares = Prestables.objects.all().order_by("-solicitudes")[:6]
    context['populares'] = populares
    return render(request, 'articulos/articulos-bavanzada.html', context)


def viewitem(request, anId):
    anItem = Prestables.objects.get(id=anId)

    if request.user.is_authenticated:

        ultimasSolicitudes = Solicitudes.objects.filter(estado_sol="Aceptada", prestable__id=anId).order_by('-tiempo_final')[:10]
        ultimasSolicitudes.values_list('tiempo_inicio', 'tiempo_final')

        if request.user.is_administrador:
            return render(request, 'articulos/viewitem_admin.html',
                          {'anItem': anItem, 'solicitudes': ultimasSolicitudes})
        else:
            return render(request, 'articulos/viewitem.html',
                          {'anItem': anItem, 'solicitudes': ultimasSolicitudes})

    return render(request, 'userSystem/home.html')


def guardar_titulo(request):

    if request.method == "POST":
        theId = request.POST.get('id')
        theTitle = request.POST.get('nombre')

        data = {
            'modificar_titulo': Prestables.objects.filter(id=theId).update(nombre=theTitle)
        }
        if data['modificar_titulo']:
            data['a_message'] = 'Titulo actualizado correctamente.'
        else:
            data['a_message'] = 'Error al actualizar el titulo.'

    return JsonResponse(data)


def guardar_descripcion(request):

    if request.method == "POST":
        theId = request.POST.get('id')
        theDescription = request.POST.get('descripcion')
        theDescription = theDescription[:200]


        data = {
            'modificar_descripcion': Prestables.objects.filter(id=theId).update(descripcion=theDescription)
        }
        if data['modificar_descripcion']:
            data['a_message'] = 'Descripcion actualizada correctamente.'
        else:
            data['a_message'] = 'Error al actualizar la descripcion.'

    return JsonResponse(data)


def cambiar_estado(request):

    if request.method == "POST":
        theId = request.POST.get('id')
        theEstado = request.POST.get('estado')

        data = {
            'modificar_estado': Prestables.objects.filter(id=theId).update(estado=theEstado)
        }
        if data['modificar_estado']:
            data['a_message'] = 'Estado actualizado correctamente.'
        else:
            data['a_message'] = 'Error al actualizar el estado.'

    return JsonResponse(data)


def cambiar_imagen(request):

    if request.method == "POST":
        theId = request.POST.get('id')
        image = request.FILES['image']
        tmp_file = os.path.join(settings.UPLOAD_PATH, image.name)
        path = default_storage.save(tmp_file, ContentFile(image.read()))

        data = {
            'modificar_imagen': Prestables.objects.filter(id=theId).update(imagen=path)
        }
        if data['modificar_imagen']:
            data['a_message'] = 'Imagen actualizada correctamente.'
        else:
            data['a_message'] = 'Error al actualizar la imagen.'

    return JsonResponse(data)


def enviar_solicitud(request):

    fechaSolicitud = datetime.now()

    if request.method == "POST":
        theId = request.POST.get('id')
        data={}

        fechaInicial = datetime.strptime(request.POST.get('fechaInicial'),"%Y/%m/%d %H:%M")
        fechaFinal = datetime.strptime(request.POST.get('fechaFinal'),"%Y/%m/%d %H:%M")
        theEmail = request.POST.get('mailUsuario')

        if(
            Solicitudes.objects.filter(estado_sol="Aceptada",tiempo_inicio__lte=fechaInicial,tiempo_final__gte=fechaInicial).count()+
            Solicitudes.objects.filter(estado_sol="Aceptada",tiempo_inicio__lte=fechaFinal,tiempo_final__gte=fechaFinal).count()>0):
            data['a_message'] = 'Ya existe una reserva aceptada en el rango de fechas indicado.'
            return JsonResponse(data)

        if (fechaInicial.weekday()>4 or
            fechaFinal.weekday() > 4 or
            fechaInicial.hour > 17 or
            fechaInicial.hour < 9 or
            fechaFinal.hour > 17 or
            fechaFinal.hour < 9):
            data['a_message'] = 'Los reservas solo pueden ser durante días hábiles entre 09 y 18 hrs.'
            return JsonResponse(data)

        if (fechaFinal - fechaInicial).total_seconds()<=0:
            data['a_message'] = 'La fecha y hora de término de la reserva debe ser posterior a la de inicio.'
            return JsonResponse(data)

        if (fechaInicial - fechaSolicitud).total_seconds()<3600:
            data['a_message'] = 'Las reservas deben ser solicitadas con un mínimo de una hora de anticipación.'
            return JsonResponse(data)

        objetoSolicitado = Prestables.objects.get(id=theId)
        personaSolicitante = Usuarios.objects.get(user__email=theEmail)

        estaSolicitud = Solicitudes(tiempo_solicitud=fechaSolicitud, tiempo_inicio=fechaInicial,
                                    tiempo_final=fechaFinal, persona=personaSolicitante, prestable=objetoSolicitado,
                                    estado_sol="Pendiente")

        try:
            estaSolicitud.save()
            data['a_message'] = 'Su solicitud se ha ingresado al sistema correctamente.'
        except:
            data['a_message'] = 'Error al procesar su solicitud.'

    return JsonResponse(data)