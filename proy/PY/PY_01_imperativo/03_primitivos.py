"""

Usa tipado dinámico, lo que significa que una variable puede tomar valores de distinto tipo.
Es fuertemente tipado, lo que significa que el tipo no cambia de manera repentina. 
Para que se produzca un cambio de tipo tiene que hacer una conversión explícita.

Tipos de datos primitivos simples:

. numbers (puede ser int o float): 0, -1, 3.14
. str: 'Hola', "Chau"
. bool: True, False

Variable:

. Espacio en la memoria de la computadora donde se almacenará un valor que podrá cambiar durante la ejecución del programa.
. Nombre: L(L | D | _)*
. El tipo de variable lo establece el contenido NO el contenedor.

"""

entero = 5
real = 3.14
string = 'Hola'
boolean = True
no_definido = None

print(type(entero), type(real), type(string), type(boolean), type(no_definido))
print(entero, real, string, boolean, no_definido)

# Conversiones
print(int('12'))
print(int(True))

print(float('3.14'))
print(float(True))

print(str(3.14))
print(str(True))

print(bool(0))
print(bool('3.14'))
print(bool('Hola'))