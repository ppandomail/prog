"""

Expresiones regulares (regex):

. Secuencia de caracteres que forman un patrón de búsqueda
. Ejemplo: correo electrónico

Patrones:

. '^Sandra' -> que empiece con ...
. 'Martin$' -> que termine con ...
. '[ñ]' -> si se encuentra en cualquier lugar el caracter ñ
. 'niñ[oa]'
. '^[O-T]' -> empiece con un caracter en el rango de O a T
. 'Ma[0-3]' -> en el rango de 0 a 3
. 'Ma[^0-3]' -> no en el rango de 0 a 3
. '.a' -> cualquier caracter

"""

import re

cadena = 'Vamos a aprender expresiones regulares'
re.search('aprender', cadena)                     # devuelve un objeto si está o None caso contrario
re.findall('aprender', cadena)                    # devuelve una lista. En este caso ['aprender']
re.match('Sandra', 'Sandra Lopez')                # devuelve True. Busca al comienzo de 'Sandra Lopez' el patrón de búsqueda
re.match('sandra', 'Sandra Lopez', re.IGNORECASE) # devuelve True 
