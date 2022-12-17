from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercicio
from .forms import ExercicioForm

# Create your views here.
def home(request):
    exercicios = Exercicio.objects.all()
    categorias = Exercicio.objects.order_by().values('categoria').distinct()
    return render(request, 'home.html', {'categorias':categorias, 'exercicios':exercicios})

def listar(request, nm):
    exercicios = Exercicio.objects.filter(categoria=nm)    
    return render(request, 'listar_ex.html', {'exercicios':exercicios, 'categoria':nm})

def criar(request):
    form = ExercicioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'form.html', {'form':form})

def editar(request, pk):
    exercicio = Exercicio.objects.get(pk=pk)
    form = ExercicioForm(request.POST or None, instance=exercicio)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'form.html', {'form':form, 'exercicio': exercicio})

def deletar(request, pk):
    exercicio = Exercicio.objects.get(pk=pk)
    exercicio.delete()
    return redirect('home')
