# Proyecto: Biblioteca (Django)

Resumen
- Proyecto de ejemplo en Django que implementa una pequeña aplicación `biblioteca` con modelos: `Autor`, `Libro` y `Resena`.
- Esta guía explica cómo poner en marcha el proyecto, crear el entorno, aplicar migraciones, poblar datos y usar el admin.

Requisitos
- Python 3.10+ (probablemente 3.12 en tu entorno actual)
- Django (la versión usada por tu entorno; se recomienda instalar en un virtualenv)
- sqlite3 (por defecto el proyecto usa `db.sqlite3`)

Entorno y virtualenv (recomendado)
1. Crear y activar un venv (si aún no lo tienes). 

Si necesitas crear uno nuevo:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias (si tienes `requirements.txt`):

```bash
pip install -r requirements.txt
```

Si no tienes `requirements.txt`, instala Django en el venv:

```bash
pip install django
```

Comandos útiles (usando el venv explícito)
- Ejecutar comandos de manage.py con el Python del venv (ejemplo con la ruta de tu entorno):

```bash
/home/sebastian_p/Documentos/Uni/P_web/Django/venv/bin/python3 /home/sebastian_p/Documentos/Uni/P_web/Django/biblioteca_project/manage.py makemigrations
/home/sebastian_p/Documentos/Uni/P_web/Django/venv/bin/python3 /home/sebastian_p/Documentos/Uni/P_web/Django/biblioteca_project/manage.py migrate
/home/sebastian_p/Documentos/Uni/P_web/Django/venv/bin/python3 /home/sebastian_p/Documentos/Uni/P_web/Django/biblioteca_project/manage.py runserver
```

Migraciones
1. Asegúrate de que la app `biblioteca` está en `INSTALLED_APPS` dentro de `biblioteca_project/settings.py`.
2. Genera y aplica migraciones:

```bash
# desde la raíz del proyecto (donde está manage.py)
/home/sebastian_p/Documentos/Uni/P_web/Django/venv/bin/python3 manage.py makemigrations
/home/sebastian_p/Documentos/Uni/P_web/Django/venv/bin/python3 manage.py migrate
```

Poblar datos (dos opciones)

Opción A — Usar fixtures (recomendado para datos estáticos):
1. Crea la carpeta `biblioteca/fixtures/` si no existe.
2. Crea un archivo `initial_data.json` (o `biblioteca_fixture.json`) con el formato de fixtures Django (JSON o YAML).
3. Carga la fixture:

```bash
/home/sebastian_p/Documentos/Uni/P_web/Django/venv/bin/python3 manage.py loaddata initial_data.json
```

Opción B — Usar un management command o script de población (recomendado para datos aleatorios):
1. Crea `biblioteca/management/commands/populate_data.py` y añade un comando que cree autores, libros y reseñas.
2. Ejecútalo con:

```bash
/home/sebastian_p/Documentos/Uni/P_web/Django/venv/bin/python3 manage.py populate_data
```

(En este repo puedo crear el comando o un script para generar 10 autores, 20 libros y 20 reseñas si quieres — dime y lo hago.)

Crear superusuario (para acceder al admin)

```bash
/home/sebastian_p/Documentos/Uni/P_web/Django/venv/bin/python3 manage.py createsuperuser
```

Estructura principal del proyecto

```
biblioteca_project/
  manage.py
  db.sqlite3
  README.md
  biblioteca/
    models.py        # Autor, Libro, Resena
    admin.py         # personalizaciones del admin
    migrations/
    fixtures/        # (opcional) guarda aquí tus fixtures
  biblioteca_project/
    settings.py
    urls.py
    wsgi.py
```

Modelos (resumen)
- `Autor`:
  - `nombre` (CharField)
  - `nacionalidad` (CharField)
- `Libro`:
  - `titulo` (CharField)
  - `autor` (ForeignKey -> Autor)
  - `fecha_publicacion` (DateField)
  - `resumen` (TextField)
- `Resena`:
  - `libro` (ForeignKey -> Libro)
  - `texto` (TextField)
  - `calificacion` (IntegerField)  <-- importante: revisar que esté definido como `models.IntegerField()`
  - `fecha` (DateTimeField auto_now_add)

Notas importantes y troubleshooting
- Error común: "sqlite3.OperationalError: no such table: biblioteca_autor" indica que no aplicaste las migraciones o que estás apuntando a una DB distinta.
  - Solución: ejecutar `makemigrations` + `migrate` con el Python del venv.
- Asegúrate de ejecutar `manage.py` desde la carpeta `biblioteca_project` (la que contiene `manage.py`) o pasando la ruta completa.
- Si `calificacion` aparece como `models.IntegerField` (sin paréntesis) corrígelo a `models.IntegerField()` y luego crea/aplica migraciones.
- Si ves "Couldn't import Django" al ejecutar `manage.py`, activa el venv o usa la ruta completa del intérprete del venv.

Admin personalizado
- `biblioteca/admin.py` ya contiene personalizaciones como `list_display`, `search_fields` y `list_filter`. Si no ves filas en el admin, comprueba que hayas poblado la BD (0 filas => la lista aparece vacía aunque la configuración de columnas exista).

Comandos útiles resumidos

```bash
# activar venv (si lo creaste):
source venv/bin/activate

# migraciones
python manage.py makemigrations
python manage.py migrate

# crear superusuario
python manage.py createsuperuser

# ejecutar servidor
python manage.py runserver

# cargar fixture
python manage.py loaddata initial_data.json

# ejecutar comando de población (si se crea)
python manage.py populate_data
```

Contribuir / próximos pasos
- Puedo crear ahora mismo:
  - Un fixture `initial_data.json` con 10 autores, 20 libros y 20 reseñas, o
  - Un comando de management `populate_data` que inserte datos aleatorios (utilizando `faker` si quieres), o
  - Ambos.

Si quieres que genere datos aleatorios con `faker`, instala `Faker` en el venv:

```bash
pip install Faker
```

Licencia
- Añade aquí la licencia que prefieras (MIT/Apache/etc.) si piensas compartir el repositorio.

Contacto
- Si quieres que automatice la creación de datos, dime la opción (fixture o management command) y lo creo.