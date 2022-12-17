from django.shortcuts import render
from .models import Exercicio, Categoria
# Create your views here.
def home(request):
    return render(request, 'home.html')

def peitoral(request):
    exercicios = Exercicio.objects.filter() #Categoria
    return render(request, 'peitoral.html', {'exercicios':exercicios})

def perna(request):
    exercicios = Exercicio.objects.filter() #Categoria
    return render(request, 'perna.html', {'exercicios':exercicios})

def costas(request):
    exercicios = Exercicio.objects.filter() #Categoria
    return render(request, 'costas.html', {'exercicios':exercicios})

    