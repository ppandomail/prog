"""

. Objetivo: persistencia de datos
. Fases necesarias para guardar información en archivos externos:
  . creación y apertura -> open(...). Modos:
    . 'r' : lectura
    . 'w' : escritura
    . 'a' : append
    . 'r+': lectura/escritura
  . lectura             -> read(...)
  . escritura           -> write(...)
  . cierre              -> close()
  
"""

from io import open

# Si el archivo no existe, el método open lo crea.
# Si el archivo existe, se reemplaza por el nuevo
fw = open('archivo.txt', 'w')    
fw.write('Hola mundo \n cruel')
fw.close()

# Si el archivo existe, append
fa = open('archivo.txt', 'a')
fa.write('\n otra línea')
fa.close()