# Django

* Es un framework de desarrollo web de código abierto y gratuito.
* Escrito en Python.
* Respeta el patrón de diseño MVC (en Dyango se llama MTV - Modelo Template Vista)
  1. T petición a V
  1. V demanda datos a M
  1. M envia datos a V
  1. V envia información a T
* Empresas que usan Django:
  * Pinterest
  * Reddit
  * Spotify
  * Instagram

## Instalación

```sh
pip install Django
```

## Crear proyecto Django

```sh
django-admin startproject <nombre-proyecto>
```

* Crea carpeta <nombre_proyecto> con los archivos: settings.py, urls.py y wsgi.py

Luego para crear BD db.sqlite3 y poner en funcionamiento el proyecto:

```sh
python manage.py migrate
```

Luego para ejecutar el servidor

```sh
python manage.py runserver
```

Abrir el navegador y escribir 127.0.0.1:8000 y nos lleva a la página de bienvenida del proyecto.

## Primera página

1. Crear y editar archivo index.py dentro de la carpeta del proyecto.

    ```py
    from django.http import HttpResponse
    import datetime

    def hola(request):
      return HttpResponse('Hola Mundo')

    def chau(request):
      return HttpResponse('Chau Mundo')
    
    def fecha(request):
      fecha_actual = datetime.datetime.now()
      documento = """ <html>
                    <body>
                      <h2> Fecha y hora actual %s </h2>
                    </body>
                    </html> """ % fecha_actual
      return HttpResponse(documento)

    def edad(request, edad, año):
      periodo = año - 2024
      edad_futura = edad + periodo
      documento = """ <html>
                      <body>
                        <h2> En el año %s tendrás %s años</h2>
                      </body>
                      </html> """ %(año, edad_futura)
      return HttpResponse(documento)
    ```

2. Editar archivo urls.py

    ```py
    from django_01_apis.index import hola, chau, fecha, edad

    urlpatterns = [
        path('admin/', admin.site.urls),    # tupla que viene por default
        path('hola/', hola),
        path('chau/', chau),
        path('fecha/', fecha),
        path('edad/<int:edad>/<int:año>', edad),
    ]
    ```

3. Ejecutar servidor de prueba

    ```sh
    python manage.py runserver
    ```

4. En navegador, introducir:
    * localhost:8000/hola/
    * localhost:8000/chau/
    * localhost:8000/fecha/
    * localhost:8000/edad/48/2030
