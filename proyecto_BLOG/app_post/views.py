from .models import Article
from django.views.generic import CreateView
from .forms import postearform
from django.urls import reverse

class publicar_post(CreateView):
    model= Article
    tamplate_name='post/publicar.html'
    form_class= postearform

    def get_success_url(self, **kwargs):
        return reverse('Pagina de inicio')