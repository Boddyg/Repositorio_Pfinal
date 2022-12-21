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
<<<<<<< HEAD
            'es_admin': 'Es admin',
            'email' : 'Correo',
            'password1' : 'contraseña',
            'password2' : 'contraseña'
=======
            'username': 'Nombre de usuario',
            'email': 'Correo',
            'password1': 'contraseña',
            'password2': 'contraseña',
>>>>>>> 71f135b78be80667e109a1dd374978cf2a96a1bd
        }
