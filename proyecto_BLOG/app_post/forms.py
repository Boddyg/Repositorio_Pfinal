from django import forms
from .models import Article, comentarios
from django.forms import ModelForm

class postearform(forms.ModelForm):
    class Meta:
        model= Article
        fields=['title', 'preview', 'content']
        labels = {
            'title': 'Titulo',
            'preview': 'Vista previa',
            'content': 'Contenido',
        }

class commentform(ModelForm):
    class Meta:
        model= comentarios
        fields= ('nombre', 'correo', 'contenido', 'active')

