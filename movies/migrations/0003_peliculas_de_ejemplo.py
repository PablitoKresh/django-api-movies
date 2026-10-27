"""Carga un catálogo de ejemplo para que la API no aparezca vacía.

Render usa SQLite y el disco se reinicia en cada despliegue, así que esta
migración vuelve a rellenar los datos cada vez que se aplican las migraciones.
"""

from django.db import migrations

PELICULAS = [
    ("El viaje de Chihiro", 2001, 125, "Animación", "Hayao Miyazaki"),
    ("El laberinto del fauno", 2006, 118, "Fantasía", "Guillermo del Toro"),
    ("Parásitos", 2019, 132, "Thriller", "Bong Joon-ho"),
    ("Origen", 2010, 148, "Ciencia ficción", "Christopher Nolan"),
    ("Pulp Fiction", 1994, 154, "Crimen", "Quentin Tarantino"),
    ("El club de la lucha", 1999, 139, "Drama", "David Fincher"),
    ("Mar adentro", 2004, 125, "Drama", "Alejandro Amenábar"),
    ("Interstellar", 2014, 169, "Ciencia ficción", "Christopher Nolan"),
    ("Toy Story", 1995, 81, "Animación", "John Lasseter"),
    ("El Padrino", 1972, 175, "Crimen", "Francis Ford Coppola"),
    ("Volver", 2006, 121, "Drama", "Pedro Almodóvar"),
    ("Matrix", 1999, 136, "Ciencia ficción", "Lana y Lilly Wachowski"),
]


def cargar(apps, schema_editor):
    Movie = apps.get_model("movies", "Movie")
    for nombre, anio, duracion, genero, director in PELICULAS:
        Movie.objects.get_or_create(
            nombre=nombre,
            defaults={
                "anio": anio,
                "duracion": duracion,
                "genero": genero,
                "director": director,
            },
        )


def borrar(apps, schema_editor):
    Movie = apps.get_model("movies", "Movie")
    Movie.objects.filter(nombre__in=[p[0] for p in PELICULAS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_alter_movie_nombre"),
    ]

    operations = [
        migrations.RunPython(cargar, borrar),
    ]
