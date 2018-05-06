from django.contrib import admin
from .models import Usuario, Prestamo, Articulo, Espacio, Reserva

admin.site.register(Usuario)
admin.site.register(Prestamo)
admin.site.register(Articulo)
admin.site.register(Espacio)
admin.site.register(Reserva)
