from django.db import models


# Create your models here.
class Articulo(models.Model):
    opciones = (
        ("Disponible", "Disponible"),
        ("En prestamo", "En prestamo"),
        ("En reparacion", "En reparacion"),
        ("Perdido", "Perdido"),
    )
    nombre = models.CharField(max_length=20)
    estado = models.CharField(max_length=15, choices=opciones, default="Disponible")
    solicitudes = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="img", default='img/none.png')

    def __str__(self):
        return self.nombre
