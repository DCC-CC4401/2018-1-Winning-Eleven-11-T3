from django.db import models


class Articulo(models.Model):
    opciones = (
        ("Disponible", "Disponible"),
        ("En prestamo", "En prestamo"),
        ("En reparacion", "En reparacion")
    )

    nombre = models.CharField(max_length=20)
    estado = models.CharField(max_length=15, choices=opciones, default="Disponible")
    solicitudes = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="img", default='img/none.png')
    espacio = models.BooleanField()
    color_calendario = models.CharField(max_length=15, default='none')


    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=256)
    permisos = models.BooleanField()

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    opciones = (
        ("Pendiente", "Pendiente"),
        ("Vigente", "Vigente"),
        ("Rechazado", "Rechazado"),
        ("Caducado", "Caducado"),
        ("Perdido", "Perdido")
    )
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=15, choices=opciones)
