import os

# os.rename(ruta1, ruta2)
# os.remove(ruta)

print(os.path.isfile('./proy/PY'))  # True si es un archivo

for f in os.listdir('.'):            # Lista de archivos y directorios
    print(f.title())

# os.mkdir(ruta)  # crea nuevo directorio
# os.chdir(ruta)  # cambia directorio actual por ruta
# os.getcwd()     # devuelve ruta directorio actual
# os.rmdir(ruta)  # borra directorio de la ruta, siempre y cuando esté vacio