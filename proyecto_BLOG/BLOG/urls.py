"""BLOG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from app_post import views as views_post



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name = 'Pagina de inicio'),
    path('post/<int:id>/', views.post_detail, name="post_detail"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('publicar/', views_post.publicar_post.as_view(template_name='post/publicar.html'), name='publicar'),
    path('acercade/', views.acercade, name = 'Acerca de')
   
]
