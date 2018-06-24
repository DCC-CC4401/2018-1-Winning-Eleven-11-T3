from django.shortcuts import render
from .models import Prestables


# Create your views here.

def viewitem(request, anId):
    context = {}
    anItem = Prestables.objects.get(id=anId)
    context['anItem'] = anItem

    populares = Prestables.objects.all()
    context['allItem'] = populares[:10]

    return render(request, 'viewitem.html', context)
    #do something with this user