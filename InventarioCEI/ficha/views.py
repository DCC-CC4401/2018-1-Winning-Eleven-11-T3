from django.shortcuts import render, redirect
from ficha.models import Prestables


# Create your views here.

def viewitem(request, anId):
    anItem = Prestables.objects.get(id=anId)

    if request.user.is_authenticated:
        if request.user.is_administrador:
            return render(request, 'ficha/viewitem_admin.html', {'anItem': anItem})
        else:
            return render(request, 'ficha/viewitem.html', {'anItem': anItem})


    return render(request, 'userSystem/home.html')