""""

Diccionarios:

. Estructura de datos que nos permiten almacenar valores de diferentes tipos (enteros, strings, decimales) e incluso listas y otros diccionarios.
. Asociación de tipo clave : valor
. Los elementos almacenados no están ordenados.

"""

dicc_vacio = {}
dicc = {'Arg':'Bs As', 'Chile':'Santiago', 'Brasil':'Brasilia'}
dicc_dicc = {'nom_full': {'nom': 'pp', 'ape': 'perez'}, 'edad': 45}

# Acceso a valores
dicc['Brasil']          # 'Brasilia'
dicc.get('Brasil')      # 'Brasilia'

# Operaciones que no modifican a un diccionario
len(dicc)     # 3
min(dicc)
max(dicc)
sum(dicc)

'España' in dicc  # False
dicc.keys()       # ['Arg', 'Chile', 'Brasil']
dicc.values()     # ['Bs As', 'Santiago', 'Brasilia']
dicc.items()

# Operaciones que modifican a un diccionario
dicc['Arg'] = 'Buenos Aires'            # agregar elemento
dicc.update({'Uruguay': 'Montevideo'})  # actualiza
dicc.pop('Uruguay')                     # elimina elemento
dicc.clear()
