from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from userSystem.models import Usuarios, User


class AdministradorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_administrador = True
        user.save()
        Usuarios.objects.create(user=user)
        return user


class UsuariosSignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UsuariosSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "email", "rut", "password1", "password2")
        help_texts = {
            'email': 'Indique su dirección de correo electrónico. Esta será usada para iniciar sesión en el sistema',
            'rut': 'Ingrese su rut, formato xx.xxx.xxx-x. Esta información será validada cuando solicite un préstamo'
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        Usuarios.objects.create(user=user)
        return user