
# Proyecto Biblioteca (Django + Django REST Framework)

Este proyecto es una biblioteca hecha con **Django** y **Django REST Framework**.
Tiene tres modelos principales:

* `Autor`
* `Libro`
* `Resena`


## Tecnologías y librerías

* Python 3.x
* Django
* Django REST Framework
* django-filter
* SQLite


## Estructura general

biblioteca_project/
  manage.py
  biblioteca/
    models.py
    admin.py
    serializers.py
    views.py
    urls.py
    pagination.py


## 1. Modelos

**Autor** → nombre y nacionalidad
Incluye una validación personalizada que evita números en la nacionalidad.

**Libro** → título, autor, fecha y resumen
El resumen debe tener una longitud mínima.

**Resena** → texto, calificación (0 a 5) y fecha creada automáticamente
Las reseñas están conectadas a los libros.


## 2. Puesta en marcha

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt   # si lo tienes
```

o instalar Django + DRF + django-filter:

```bash
pip install django djangorestframework django-filter markdown
```

Migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

Superuser:

```bash
python manage.py createsuperuser
```

Servidor:

```bash
python manage.py runserver
```

Admin:

```
http://127.0.0.1:8000/admin/
```

## 3. Serializers


Los serializers convierten objetos Python ↔ JSON.

Usé `ModelSerializer` porque es más fácil.

### Qué es `SerializerMethodField`

Es un campo que NO existe en el modelo, pero que yo calculo “a mano” desde el serializer.

Ejemplo claro:

* Últimos libros de un autor
* Últimas reseñas de un libro

### Fragmento real:

```python
libros_recientes = serializers.SerializerMethodField()

def get_libros_recientes(self, obj):
    libros = obj.libros.order_by('-fecha_publicacion')[:5]
    return LibroSerializer(libros, many=True).data
```


## 4. ViewSets

En DRF, un `ModelViewSet` te da CRUD completo sin escribir todo a mano.

Estructura:

* `AutorViewSet`
* `LibroViewSet`
* `ResenaViewSet`

### Incorporaciones:

#### Filtros (`filterset_fields`)

Permite filtrar desde la URL:

```
/api/libros/?autor=1
/api/autores/?nacionalidad=Colombiano
```

#### Ordenamiento (`ordering_fields`)

```
/api/libros/?ordering=titulo
/api/libros/?ordering=-fecha_publicacion
```

#### Paginación personalizada

```
/api/libros/?page=2&per_page=15
```

#### Ruta personalizada con @action

Promedio de calificaciones de un libro:

```
/api/libros/3/promedio_calificaciones/
```

---

## 5. Cómo está estructurada la API

Rutas base:

```
/api/autores/
/api/libros/
/api/resenas/
```

Cada una soporta:

* GET (lista)
* POST (crear)
* GET /id (detalle)
* PUT/PATCH (editar)
* DELETE (eliminar)

### Para probar:

Navegador de DRF o Postman.
