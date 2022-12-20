from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.

class registroUsuario(CreateView):
    model=User
    template_name='templates/singup.html'
    form_class=UserCreationForm
    success_url= redirect('inicio/')
    