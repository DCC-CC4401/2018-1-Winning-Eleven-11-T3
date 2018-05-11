from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)  # changes email to unique and blank to false
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS
    is_user = models.BooleanField(default=False)
    is_administrador = models.BooleanField(default=False)
    has_permission = models.BooleanField(default=True)
    rut = models.CharField(max_length=30, unique=True, default="")



class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username