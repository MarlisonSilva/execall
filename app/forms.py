from django.utils.translation import gettext_lazy as _
from django import forms
from .models import *

class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['nome', 'carga', 'categoria']
