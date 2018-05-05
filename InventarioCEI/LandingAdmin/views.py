from django.shortcuts import render
from .models import Producto


def index(request):
    error_message = ""
    if request.method == 'POST':
        #agregar
        if request.POST.get('agregar', False):
            nombre_producto = request.POST['agregar']
            productoYaListado = Producto()
            try:
                productoYaListado = Producto.objects.get(nombre=nombre_producto)
                if productoYaListado:
                    error_message = "El producto ya existe en el inventario"
            except productoYaListado.DoesNotExist:
                if nombre_producto == "":
                    error_message = "El producto debe de tener un nombre no vacio"
                else:
                    producto = Producto(nombre=nombre_producto, cantidad=5)
                    producto.save()
        #quitar
        elif request.POST.get('quitar',False):
            producto = Producto.objects.get(pk=request.POST['quitar'])
            producto.delete()
        #restar
        elif request.POST.get('restar',False):
            producto = Producto.objects.get(pk=request.POST['restar'])
            if producto.cantidad == 0:
                error_message = "El producto no puede tener una cantidad negativa de unidades"
            else:
                producto.cantidad -= 1
                producto.save()
        #sumar
        elif request.POST.get('sumar',False):
            producto = Producto.objects.get(pk=request.POST['sumar'])
            producto.cantidad += 1
            producto.save()

    return render(request, 'inventario/index.html', {'all_objects': Producto.objects.all(),
                                                     'error_message': error_message})
