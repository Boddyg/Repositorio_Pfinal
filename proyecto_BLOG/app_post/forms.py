from django import forms
from .models import Article

class postearform(forms.ModelForm):
    class Meta:
        model= Article
        fields=['title', 'preview', 'content']
        labels = {
            'title': 'Titulo',
            'preview': 'Vista previa',
            'content': 'Contenido',
        }