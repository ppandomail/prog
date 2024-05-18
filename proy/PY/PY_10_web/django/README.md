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

    def saludo(request):
      return HttpResponse('Hola Mundo')

    def despedida(request):
      return HttpResponse('Adiós mundo cruel')
    ```

2. Editar archivo urls.py

    ```py
    from proy_django.index import saludo, despedida

    urlpatterns = [
        path('admin/', admin.site.urls),    # tupla que viene por default
        path('saludo/', saludo),
        path('chau/', despedida),
    ]
    ```

3. Ejecutar servidor de prueba

    ```sh
    python manage.py runserver
    ```

4. En navegador, introducir:
    * localhost:8000/saludo/
    * localhost:8000/chau/
