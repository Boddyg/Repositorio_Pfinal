
from django.shortcuts import render, get_object_or_404, redirect
from app_post.models import Article
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from app_post.models import comentarios
from app_post.forms import commentform
from usuarios.forms import FormularioRegistro


def inicio(request):
	posts = Article.objects.all()

	return render(request, 'index.html', {'posts': posts})

def post_detail(request, id):
        post = get_object_or_404(Article, id=id)
        coments= post.comments.all()
        if request.method == 'POST':
            form= commentform(request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.post = post
                new_form.save()
        else:
            form=commentform
        return render(request, 'post_details.html', {"post": post, 'comments': coments, 'form': form})

def register(request):
    if request.method == 'POST':

    	# Assigning the User Creation form with the Post request object to form variable
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            # Save the user
            form.save()
            # Getting the values from the form
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authenticate user using the authenticate method
            user = authenticate(username=username, password=raw_password)

            # After Successfully Authenticated then use login function to login the user

            login(request, user)
            return redirect('/')
    else:
        form = FormularioRegistro()
    return render(request, 'singup.html', {'form': form})

def acercade(request):
        return render(request, "acercade.html", {})
        