from django.contrib import admin
from .models import Prestables, Prestamos, Solicitudes, Aforo, Profile

admin.site.register(Prestables)
admin.site.register(Prestamos)
admin.site.register(Solicitudes)
admin.site.register(Aforo)
admin.site.register(Profile)
