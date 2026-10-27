from rest_framework.routers import APIRootView, DefaultRouter

from .views import MovieViewSet


class InicioAPI(APIRootView):
    """
    API REST para gestionar un catálogo de películas, hecha con Django REST Framework.

    Cada película tiene título (`nombre`), año (`anio`), duración en minutos (`duracion`),
    género y director. Pulsa en el enlace de `movies` para ver el catálogo, buscar,
    ordenar o añadir una película desde el formulario de abajo.

    Los datos se reinician en cada despliegue, así que puedes probar sin miedo.
    """

    def get_view_name(self):
        return "API de películas"


class Router(DefaultRouter):
    APIRootView = InicioAPI


router = Router()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = router.urls
