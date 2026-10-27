from django.db.models.functions import Lower
from rest_framework import filters, viewsets

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    Catálogo de películas.

    - `GET /movies/` lista las películas (10 por página).
    - `POST /movies/` crea una película nueva.
    - `GET /movies/{id}/` muestra una película; `PUT`, `PATCH` y `DELETE` la modifican o la borran.

    Búsqueda: `?search=nolan` busca en título, director y género.
    Orden: `?ordering=-anio` (también `anio`, `duracion`, `nombre`).
    """

    queryset = Movie.objects.all().order_by(Lower("nombre"))
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nombre", "director", "genero"]
    ordering_fields = ["nombre", "anio", "duracion"]

    def get_view_name(self):
        if self.suffix == "Instance":
            return "Película"
        return "Películas"
