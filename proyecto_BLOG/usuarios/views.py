from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.views.generic import CreateView
from .forms import FormularioRegistro


# Create your views here.

class registroUsuario(CreateView):
    model=User
    template_name='templates/singup.html'
    form_class=FormularioRegistro
    