import os

print(os.environ)        # Lista de variables de entorno
print(os.getenv('PATH')) # Valor de variable de entorno
print(os.sep)            # Separador. Ejemplo: /
print(os.getcwd())       # Directorio de trabajo

# os.remove('main.py')   # Elimina archivo