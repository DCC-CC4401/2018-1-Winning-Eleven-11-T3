from django.db import models


class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    estado = models.IntegerField()     #0,1,2,3
    imagen = models.CharField(max_length=256)
    cantidad = models.IntegerField()

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
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.IntegerField()

