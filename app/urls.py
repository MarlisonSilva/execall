"""projeto URL Configuration

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
from app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('execs/<str:nm>/', views.listar, name='exercicio.listar'),
    path('ex/c/', views.criar, name='exercicio.criar'),
    path('ex/e/<int:pk>/', views.editar, name='exercicio.editar'),
    path('ex/d/<int:pk>/', views.deletar, name='exercicio.deletar'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),

]
