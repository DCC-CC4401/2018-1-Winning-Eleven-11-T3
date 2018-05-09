from django.db import models
from django.contrib.auth.models import User
import uuid
from random import randint

# Clase prestables, pueden ser articulos o salas
class Prestables(models.Model):

    #falta resolver el ID, si usar randint o uuid
    id =  models.IntegerField(primary_key=True, default=randint(10000000,99999999), editable=False)

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

    def __str__(self):
        return self.nombre

# Para espacios, detalle de la cantidad de asistentes maxima
class Aforo(models.Model):
    id = models.ForeignKey(Prestables, on_delete=models.CASCADE)
    capacidad = models.IntegerField(primary_key=True)


#esto es para extender el modelo de usuarios
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.IntegerField(primary_key=True,unique=True)

    #lo puse como integer, al usuario se le pide sin puntos ni guion



# todas las solicitudes, pendientes, aceptadas o rechazadas
class Solicitudes(models.Model):
    opciones_sol = (
        ("Pendiente", "Pendiente"),
        ("Aceptada", "Aceptada"),
        ("Rechazada", "Rechazada"),
    )

    id = models.IntegerField(primary_key=True, default=randint(10000000,99999999), editable=False)
    tiempo_inicio = models.DateTimeField
    tiempo_final = models.DateTimeField
    rut_per = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_obj = models.ForeignKey(Prestables, on_delete=models.CASCADE)
    estado_sol = models.CharField(max_length=15, choices=opciones_sol)


# Prestamos, solicitudes aceptadas
class Prestamos(models.Model):

    opciones_pres = (
        ("Vigente", "Vigente"),
        ("Caducada", "Caducada"),
        ("Perdida", "Perdida"),
    )

    id = models.OneToOneField(Solicitudes, on_delete=models.CASCADE,primary_key=True)
    estado_sol = models.CharField(max_length=15, choices=opciones_pres)

