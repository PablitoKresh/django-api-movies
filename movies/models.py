from django.db import models

#Creacion del modelo Movie con sus atributos correspondientes

class Movie(models.Model):
    nombre = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    duracion = models.PositiveIntegerField()
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.anio})"