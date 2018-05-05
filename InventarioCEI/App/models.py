from django.db import models


# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.CharField(max_length=10)
    solicitudes = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="img", default='img/none.png')
