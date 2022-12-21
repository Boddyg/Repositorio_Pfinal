from .models import Article
from django.views.generic import CreateView
from .forms import postearform
from django.urls import reverse
from core.mixins import adminRequired

class publicar_post(adminRequired, CreateView):
    model= Article
    tamplate_name='post/publicar.html'
    form_class= postearform

    def get_success_url(self, **kwargs):
        return reverse('Pagina de inicio')