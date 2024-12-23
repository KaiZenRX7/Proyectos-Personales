from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.JSONField(default=list ,null=True, blank=True)
    habilidades = models.JSONField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    altura = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    evolucion = models.CharField(max_length=100, blank=True)
    imagen = models.URLField(max_length=200, null=True, blank=True)
    hp = models.IntegerField(blank=True, null=True)
    ataque = models.IntegerField(blank=True, null=True)
    defensa = models.IntegerField(blank=True, null=True)
    ataque_especial = models.IntegerField(blank=True, null=True)
    defensa_especial = models.IntegerField(blank=True, null=True)
    velocidad = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre


class Entrenador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100, blank=True, null=True)
    pokemons = models.ManyToManyField(Pokemon, blank=True)
    es_ficticio = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def can_add_pokemon(self):
        return self.pokemons.count() < 6