"""

Serialización:

. Guardar en un archivo una colección, un objeto en formato de código binario.
. Biblioteca: pickle
  . método dump() : volcado de datos al archivo binario externo.
  . método load() : carga de los datos del archivo binario externo.

"""

import pickle

lista = ['Pedro', 'Ana', 'Maria', 'Isabel']
arch = open('archivo', 'wb')
pickle.dump(lista, arch)
arch.close()


arch = open('archivo', 'rb')
lista = pickle.load(arch)
print(lista)
arch.close()
