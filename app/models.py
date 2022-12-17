from django.db import models

# Create your models here.
class Exercicio(models.Model):
  CATEGORIAS = (
    ("Peitoral", "Peitoral"),
    ("Pernas", "Pernas"),
    ("Costas", "Costas"),
    ("Bíceps", "Bíceps"),
    ("Tríceps", "Tríceps"),
  )

  nome = models.CharField(max_length=100)
  carga = models.IntegerField()
  data = models.DateField(auto_now_add=True)
  categoria = models.CharField(max_length=50, choices=CATEGORIAS, null=True, blank=True)
  
  class Meta:
    verbose_name_plural = 'Exercícios'
    ordering = ('categoria',)

  def __str__ (self):
    return self.nome