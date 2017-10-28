from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Setor(models.Model):
    nome = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)

    def __str__(self):
        return self.nome + " - " + self.cidade


class Colaborador(User):

    foto = models.ImageField(upload_to='users', default='no-image-box.png', blank=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    setor = models.ForeignKey(Setor)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Produto(models.Model):

    nome = models.CharField(max_length=30)
    patrimonio = models.CharField(max_length=10)
    nota_fiscal = models.CharField(max_length=10)
    colaborador = models.ForeignKey(Colaborador)

    def __str__(self):
        return self.nome
