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

# En el navegador introducir -> localhost:8000/edades/48/2030
def edad(request, edad, año):
  periodo = año - 2024
  edad_futura = edad + periodo
  documento = """ <html>
                  <body>
                    <h2> En el año %s tendrás %s años</h2>
                  </body>
                  </html> """ %(año, edad_futura)
  return HttpResponse(documento)
