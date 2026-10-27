# 🎬 API REST de películas

API REST para gestionar un catálogo de películas, construida con **Django REST Framework**.

👉 **Pruébala en vivo:** [api.pablobertolet.dev](https://api.pablobertolet.dev)
(la interfaz navegable de DRF permite listar, buscar y añadir películas desde el navegador)

---

## ✨ Funcionalidades

- **CRUD completo** sobre el recurso `movies` mediante un `ModelViewSet` y un `router` de DRF.
- **Búsqueda** por título, director y género: `?search=nolan`
- **Ordenación** por título, año o duración: `?ordering=-anio`
- **Paginación** de 10 resultados por página.
- **Datos de ejemplo** cargados con una migración, para que la API no aparezca vacía tras cada despliegue.
- Vista raíz personalizada con la documentación de uso.

## 📌 Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/movies/` | Lista paginada de películas |
| `POST` | `/movies/` | Crea una película |
| `GET` | `/movies/{id}/` | Detalle de una película |
| `PUT` / `PATCH` | `/movies/{id}/` | Modifica una película |
| `DELETE` | `/movies/{id}/` | Elimina una película |

### Modelo `Movie`

| Campo | Tipo | Notas |
|---|---|---|
| `nombre` | texto (100) | Único |
| `anio` | entero positivo | Año de estreno |
| `duracion` | entero positivo | Minutos |
| `genero` | texto (100) | |
| `director` | texto (100) | |

Ejemplo de petición:

```bash
curl -X POST https://api.pablobertolet.dev/movies/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Alien", "anio": 1979, "duracion": 117, "genero": "Ciencia ficción", "director": "Ridley Scott"}'
```

## 🛠️ Tecnologías

- Python · Django 5 · Django REST Framework
- SQLite
- WhiteNoise (estáticos) y Gunicorn
- Despliegue en **Render** con dominio propio

## 🚀 Ejecutar en local

```bash
git clone https://github.com/PablitoKresh/django-api-movies.git
cd django-api-movies

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate        # crea la BD y carga las películas de ejemplo
python manage.py runserver
```

La API queda disponible en `http://127.0.0.1:8000/`.

## 📁 Estructura

```
api_movies_rest/   configuración del proyecto Django
movies/            app: modelo, serializer, viewset, rutas y migraciones
templates/         plantilla personalizada de la API navegable
```

---

Hecho por **Pablo Jiménez Bertolet** · [Portfolio](https://www.pablobertolet.dev) · [LinkedIn](https://www.linkedin.com/in/pablo-jimenez-bertolet/)
