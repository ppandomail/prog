# Entrada por terminal
age = input('Cual es tu edad? ')  # siempre devuelve una cadena

# Salida por terminal
# print(dato1, ..., sep=' ', end='\n', file=sys.stdout)
print('Tu edad es', age)
print('Tu edad es', age, sep='->')
print('Tu edad es', age, end='!\n')

dia = 9
mes = "noviembre"
print(f"Mi cumple es el {dia} de {mes}")