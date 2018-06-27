from django.contrib import admin
from .models import Prestables, Prestamos, Solicitudes, Aforo

# Register your models here.

admin.site.register(Prestables)
admin.site.register(Prestamos)
admin.site.register(Solicitudes)
admin.site.register(Aforo)
