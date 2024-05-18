from io import open

arch = open('archivo.txt', 'r')
texto = arch.read()           # devuelve todo el contenido del archivo
arch.close()
print(texto)

arch = open('archivo.txt', 'r')
lineas = arch.readlines()     # devuelve lista
arch.close()
print(lineas[0])
print(lineas[1])

arch = open('archivo.txt', 'r')
print(arch.read())
arch.seek(0)         # se cambia posición del puntero al caracter en posición 0
print(arch.read())
arch.read(11)        # lee hasta el caracter en posición 11 

arch = open('archivo.txt', 'r+')
arch.write('Comienzo del texto')
lista = arch.readlines()
lista[1] = 'linea incluida desde el exterior \n'
arch.seek(0)
arch.writelines(lista)
arch.close()