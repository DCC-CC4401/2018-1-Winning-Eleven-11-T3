from django.contrib import admin
from .models import Usuario, Prestamo, Articulo

admin.site.register(Usuario)
admin.site.register(Prestamo)
admin.site.register(Articulo)