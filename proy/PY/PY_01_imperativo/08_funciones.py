"""

Función:

. Es un bloque de código que tiene asociado un nombre
. Funcionan como una unidad realizando una tarea específica
. Pueden devolver valor
. Pueden tener parámetros/argumentos (el pasaje es siempre por referencia)
. Se las denomina "métodos" cuando se encuentran definidas dentro de una clase
. Utilidad: reutilización de código

"""


def sumar(a, b=3):      # declaración con argumento por defecto
    return a + b        # cuerpo

print(sumar(1, 2))      # argumentos posicionales
print(sumar(b=2, a=1))  # argumentos nominales
print(sumar(1))


def sum_all(*varargs):  # argumentos variables
    suma = 0
    for v in varargs:
        suma += v
    return suma

print(sum_all(1, 2, 3, 4, 5))


def text_preview(original_text, words=30):
    word_list = original_text.split()
    preview = ' '.join(word_list[:words])
    return f'{preview}...'

print(text_preview('Could not find a version that satisfies the requirement request ', 4))