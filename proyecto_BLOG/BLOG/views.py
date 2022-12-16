
from django.shortcuts import render, get_object_or_404
from app_post.models import Article


def inicio(request):
	posts = Article.objects.all()
	return render(request, 'index.html', {'posts': posts})

def post_detail(request, id):
	post = get_object_or_404(Article, id=id)

	return render(request, 'post_details.html', {"post": post})

