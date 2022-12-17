from django.db import models

# Create your models here.

class Categoria(models.Model):
  nome = models.CharField(max_length=100)

  class Meta:
    verbose_name_plural = 'Categorias'

  def __str__ (self):
    return self.nome


class Exercicio(models.Model):
  nome = models.CharField(max_length=100)
  carga = models.IntegerField()
  data = models.DateField(auto_now_add=True)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Exercícios'

  def __str__ (self):
    return self.nome