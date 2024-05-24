'''

shutil:

. Provee funciones para realizar operaciones sobre directorios en el sistema
. El módulo se encuentra en la biblioteca Python

'''

import shutil

shutil.move('users/documents/python/main.py', 'users/documents/main.py')
shutil.copy('users/documents/python/main.py', 'users/documents/main.py')
shutil.rmtree('settings')  # Elimina directorio
