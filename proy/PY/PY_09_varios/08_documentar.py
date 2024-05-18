"""

Documentar un programa:

. Es incluir comentarios en clases, métodos, módulos, etc.
. Para ayudar en el trabajo en equipo
. Especialmente útil en aplicaciones complejas

"""

def area_cuadrado(lado):
  """ Calcula el área de un cuadrado
  elevando al cuadrado el lado pasado
  por parámetro """
  return "El area es: " + str(lado * lado)

print(area_cuadrado.__doc__)  # imprime comentario
help(area_cuadrado)            # imprime mas detalle

