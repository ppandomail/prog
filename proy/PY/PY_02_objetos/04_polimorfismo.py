"""

Polimorfismo:

. Objetos responden al mismo mensaje (mismo comportamiento). Ejemplo: "apagar"
. En tiempo de ejecución sabe a que método "m" invocar dependiendo del tipo de objeto.

"""

class A:
  def m(self):
    print('soy A')

class B:
  def m(self):
    print('soy B')

class C:
  def m(self):
    print('soy C')

def hacer(x):
  x.m()

hacer(A())
hacer(B())
hacer(C())
