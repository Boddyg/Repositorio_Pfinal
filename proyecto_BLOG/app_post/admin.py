from django.contrib import admin
from .models import Article, comentarios



# Register your models here.


# To register this Article Model in our Admin interface
admin.site.register(Article)
admin.site.register(comentarios)