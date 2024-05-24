"""

Algoritmo:

. Es un conjunto de pasos o procedimientos utilizados para resolver un problema.
. Es un proceso bien definido que toma alguna entrada, realiza ciertas operaciones en la entrada y 
  produce alguna salida.

Complejidad de los algoritmos:

. Es una medida de cuán eficiente es el algoritmo para resolver el problema. 
. En otras palabras, es una medida de cuánto tiempo y espacio (memoria) requiere el algoritmo 
  para producir una solución.

Formas de medir la complejidad:

. C. Temporal T(n): contar el número de operaciones básicas (como sumas o multiplicaciones) que realiza el algoritmo. 
. C. Espacial E(n): contar la cantidad de memoria (en bytes o bits) que requiere el algoritmo.

Notación O grande:

. Proporciona una forma de comparar la complejidad de diferentes algoritmos.
. Por ejemplo, un algoritmo con una T(n) de O(n) se considera más eficiente que un algoritmo 
  con una T(n) de O(n^2), porque crece a un ritmo más lento a medida que aumenta el tamaño de entrada.
  
. Excelente: O(1)
. Bueno: O(log n)
. Regular: O(n)
. Malo: O(n log n)
. Horrible: O(n^2), O(2^n), O(n!)

En general, el objetivo del diseño de algoritmos es encontrar algoritmos que sean eficientes y fáciles de implementar.

Ejemplo: búsqueda en lista ordenada 
https://www.europeanvalley.es/noticias/la-complejidad-de-los-algoritmos/
"""

import random
import time
import matplotlib.pyplot as plt

lista = random.sample(range(1, 15000000), 9000000)
lista.sort()

tiempos_seq = []
tiempos_bin = []
encontrados = 0

def bseq(search):
    global encontrados
    for i in range(0, len(lista)):
        if lista[i] == search:
            encontrados = encontrados + 1
            break

def bbin(search):
    ini = 0
    fin = len(lista)
    med = 0
    while ini < fin :
        med = (fin + ini) // 2
        if lista[med] < search :
            ini = med + 1
        elif lista[med] > search :
            fin = med - 1
        else:
            break

for _ in range(0, 100):
    search = random.randint(1, 15000000)
    start_time = time.time()
    bseq(search)
    end_time = time.time()
    tiempos_seq.append(end_time - start_time)
    
    start_time = time.time()
    bbin(search)
    end_time = time.time()
    tiempos_bin.append(end_time - start_time)

print("valores encontrados ", encontrados)
fig, ax = plt.subplots(figsize=(12, 8))
ax.set(title= "Comparación algoritmos de búsqueda \nSecuencial vs Binario",
       ylabel= "Tiempos de búsqueda\n(segundos)",
       xlabel= "Número de búsquedas")

ax.plot(tiempos_seq, color="red", marker="o")
ax.plot(tiempos_bin, color="blue")
ax.legend(["Secuencial", "Binario"])
plt.show()

