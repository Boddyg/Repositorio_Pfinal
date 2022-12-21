from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario

class FormularioRegistro(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ["username", "email", "password1", "password2", "telefono" ]
        labels = {
            'telefono' : 'Teléfono:',
            'username': 'Nombre de usuario',
            'email': 'Correo',
            'password1': 'contraseña',
            'password2': 'contraseña',
        }
