from django.shortcuts import render
from .models import Articulo


# Create your views here.

def viewitem(request, anId):
    anItem = Articulo.objects.get(id=anId)
    return render(request, 'viewitem.html', {'anItem': anItem})
    #do something with this user