from django.shortcuts import render, redirect
from ficha.models import Prestables
from django.http import JsonResponse
import os

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def viewitem(request, anId):
    anItem = Prestables.objects.get(id=anId)

    if request.user.is_authenticated:
        if request.user.is_administrador:
            return render(request, 'ficha/viewitem_admin.html', {'anItem': anItem})
        else:
            return render(request, 'ficha/viewitem.html', {'anItem': anItem})


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