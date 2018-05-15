from django.db import models
from django.contrib.auth.models import User
import uuid
from random import randint

# Clase prestables, pueden ser articulos o salas
class Prestables(models.Model):

    #falta resolver el ID, si usar randint o uuid
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


#esto es para extender el modelo de usuarios
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=30,primary_key=True,unique=True)



# todas las solicitudes, pendientes, aceptadas o rechazadas
class Solicitudes(models.Model):
    opciones_sol = (
        ("Pendiente", "Pendiente"),
        ("Aceptada", "Aceptada"),
        ("Rechazada", "Rechazada"),
    )

    id = models.BigAutoField(primary_key=True)
    tiempo_inicio = models.DateTimeField
    tiempo_final = models.DateTimeField
    tiempo_solicitud = models.DateTimeField
    persona = models.OneToOneField(Profile, on_delete=models.CASCADE, default=None)
    prestable = models.OneToOneField(Prestables, on_delete=models.CASCADE, default=None)
    estado_sol = models.CharField(max_length=15, choices=opciones_sol)

    def save(self):
        if not self.id:
            is_unique = False
            while not is_unique:
                id = randint(1000000000, 9999999999)  # 19 digits: 1, random 18 digits
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

