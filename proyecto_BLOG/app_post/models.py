from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):

	title = models.CharField(max_length=200)
	preview = models.TextField(max_length=500)
	content = models.TextField(max_length=1000)
	posted = models.DateTimeField(auto_now_add=True)
	
	def publicar(self):
		self.posted = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class comentarios(models.Model):
	post=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
	nombre=models.CharField(max_length=150)
	correo=models.EmailField()
	contenido= models.TextField(max_length=600)
	creado_en=models.DateField(auto_now_add=True)
	active=models.BooleanField(default=False)
	
	def __str__(self):
		return f'Comentario de {self.nombre} {self.contenido}'