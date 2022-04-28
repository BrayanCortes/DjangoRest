from enum import unique
import re
from django.db import models

# Create your models here.


class Alimento(models.Model):
    id = models.AutoField(primary_key=True)
    NombreAlimento= models.CharField(max_length=100,unique=True)
    Categoria = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.NombreAlimento


class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    NombrePlato=models.CharField(max_length=100,unique=True)
    Tiempo_Pre=models.IntegerField()
    CategoriaP=models.CharField(max_length=100)
    alimento = models.ManyToManyField(Alimento)

