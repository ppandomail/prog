"""
 
 Herencia múltiple:

. Cuando hay herencia múltiple se dá preferencia a la 1ra clase que se indique en la declaración.
. Ante el problema si varias superclases tienen los mismos atributos o métodos.
. En el ejemplo, la clase A.   
    
"""

class A:
  
  def m(self):
      return "soy m de la clase A"

class B:
    
  def m(self):
      return "soy m de la clase B"

class C(A, B):
  pass

c = C()
print(isinstance(c, C))  # True
print(isinstance(c, A))  # True
print(c.m())             # "soy m de la clase A"