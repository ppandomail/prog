'''

La ofuscación es una práctica que permite modificar el código 
de forma que éste se vuelva ilegible para otros desarrolladores. 

pip install PyObfuscator

'''

from PyObfuscator import Obfuscator

Obfuscator("lib_pyobfuscator.py", deobfuscate=False, level=2).default_obfuscation()

# level=1 nombres de variables cambiadas + doc y signature es borrado
# level=2 level 1 + strings son encriptados
# level=3 level 2 + código es comprimido usando GZIP
