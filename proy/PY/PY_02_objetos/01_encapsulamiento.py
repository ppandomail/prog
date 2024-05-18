"""

POO:

. Todo es pensando como un objeto.
. Los objetos tienen: comportamiento (métodos) y propiedades (atributos)


Clase:

. Modelo donde se redactan las características comunes de un grupo de objetos.
. Es la plantilla, el molde, la fábrica de hacer objetos.
. Objeto que tiene como responsabilidad crear objetos del mismo tipo.

Objeto: 

. Ejemplar perteneciente a una clase. Instancia de clase.

Encapsulamiento:

. Objetivo: ocultar detalles de implementación.
. Funcionamiento interno protegido del exterior para que nadie pueda acceder y manipularlo.

"""

class Auto:
  
  # Constructor: inicializa los atributos del objeto
  # self: es el objeto actual
  def __init__(self, ruedas=4):
    # Atributos
    self.__ruedas = ruedas
    self.__enmarcha = False

  # Métodos
  def arrancar(self):
    self.__enmarcha = True
  
  def get_estado(self):
    if self.__enmarcha:
      return 'En marcha'
    else:
      return 'Parado'
  
  # Método privado: solo puede ser invocado dentro de la clase. Sino: AttributeError 
  def __chequeo_interno(self):
    pass

miAuto = Auto()
print(miAuto.get_estado())
miAuto.arrancar()
miAuto.__enmarcha = False    # no hay error, tampoco modifica porque está encapsulado
print(miAuto.get_estado())
