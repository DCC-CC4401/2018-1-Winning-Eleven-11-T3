from django.db import models
from random import randint
from django.utils import timezone
from userSystem.models import Usuarios, User
import uuid


# Create your models here.
class Prestables(models.Model):
    # falta resolver el ID, si usar randint o uuid
    id = models.BigAutoField(primary_key=True)

    opciones = (
        ("Disponible", "Disponible"),
        ("En prestamo", "En prestamo"),
        ("En reparacion", "En reparacion"),
        ("Perdido", "Perdido"),
    )
    nombre = models.CharField(max_length=20)
    estado = models.CharField(max_length=15, choices=opciones, default="Disponible")
    imagen = models.ImageField(upload_to="img", default='img/none.png')
    descripcion = models.CharField(max_length=200, default="")
    numsolic = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    def save(self):
        if not self.id:
            is_unique = False
            while not is_unique:
                id = randint(1000000000, 1999999999)  # 19 digits: 1, random 18 digits
                is_unique = (Prestables.objects.filter(id=id).count() == 0)
            self.id = id
        super(Prestables, self).save()


# Para espacios, detalle de la cantidad de asistentes maxima
class Aforo(models.Model):
    espacio = models.OneToOneField(Prestables, on_delete=models.CASCADE, default=None)
    capacidad = models.IntegerField(default=0)


# todas las solicitudes, pendientes, aceptadas o rechazadas
class Solicitudes(models.Model):
    opciones_sol = (
        ("Pendiente", "Pendiente"),
        ("Aceptada", "Aceptada"),
        ("Rechazada", "Rechazada"),
    )

    id = models.CharField(primary_key=True, default="", max_length=50)
    tiempo_inicio = models.DateTimeField(blank=False, default=timezone.now)
    tiempo_final = models.DateTimeField(blank=False, default=timezone.now)
    tiempo_solicitud = models.DateTimeField(blank=False, default=timezone.now)
    persona = models.ForeignKey(Usuarios, on_delete=models.CASCADE, default=None)
    prestable = models.ForeignKey(Prestables, on_delete=models.CASCADE, default=None)
    estado_sol = models.CharField(max_length=15, choices=opciones_sol)

    def save(self):
        if not self.id:
            is_unique = False
            while not is_unique:
                id = str(uuid.uuid4())
                is_unique = (Solicitudes.objects.filter(id=id).count() == 0)
            self.id = id
        super(Solicitudes, self).save()


# Prestamos, solicitudes aceptadas
class Prestamos(models.Model):

    opciones_pres = (
        ("Vigente", "Vigente"),
        ("Caducada", "Caducada"),
        ("Perdida", "Perdida"),
    )

    solicitud_aceptada = models.OneToOneField(Solicitudes, on_delete=models.CASCADE,primary_key=True)
    estado_sol = models.CharField(max_length=15, choices=opciones_pres)
