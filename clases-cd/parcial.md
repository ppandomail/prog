# Parcial

1. ¿Qué representa realmente el "tipado dinámico" en Python?
    * [ ] El tipo de una variable depende del compilador.
    * [ ] El tipo de una variable debe declararse antes de su uso.
    * [x] El tipo de una variable depende del valor asignado y puede cambiar dinámicamente.
    * [ ] Todas las variables son de tipo str por defecto.

2. ¿Cuál es la diferencia principal entre listas y tuplas en Python?
    * [ ] No existen diferencias, ambas estructuras funcionan igual.
    * [x] Las listas son ordenadas y mutables; las tuplas son ordenadas e inmutables.
    * [ ] Las tuplas se almacenan como claves-valor.
    * [ ] Las listas no permiten tipos de datos heterogéneos.

3. ¿Qué función cumple el operador % en Python?
    * [ ] Multiplicación.
    * [ ] División entera.
    * [x] Resto de una división.
    * [ ] Potencia.

4. ¿Cuál de los siguientes operadores se usa para verificar si dos referencias apuntan al mismo objeto en memoria?
    * [ ] ==
    * [ ] !=
    * [x] is
    * [ ] in

5. ¿Qué sucede si una función recursiva en Python no tiene una condición de parada adecuada?
    * [ ] Termina exitosamente después de 100 llamadas.
    * [x] Produce un RecursionError al exceder el límite de llamadas recursivas.
    * [ ] Lanza un ValueError.
    * [ ] Se convierte en un bucle infinito sin errores.

6. ¿Cuál es la salida del siguiente código? print('Hola', end='!')
    * [ ] Hola
    * [x] Hola!
    * [ ] ¡Hola!
    * [ ] Error de sintaxis

7. ¿Qué hace el siguiente código list('Python')?
    * [ ] Devuelve una lista con un solo elemento 'Python'.
    * [x] Devuelve una lista con cada carácter de 'Python' como un elemento.
    * [ ] Devuelve una lista vacía.
    * [ ] Genera un error.

8. ¿Cuál es una característica de las funciones anónimas (lambda) en Python?
    * [ ] Son funciones almacenadas permanentemente como variables globales.
    * [x] Son funciones que no tienen nombre y se definen en una sola línea.
    * [ ] Son funciones recursivas por defecto.
    * [ ] Son funciones que requieren múltiples líneas de código.

9. ¿Qué tipo de colección en Python no permite claves duplicadas?
    * [ ] Lista (list)
    * [ ] Tupla (tuple)
    * [x] Diccionario (dict)
    * [ ] Conjunto (set)

10. ¿Qué significa realmente input() en Python?
    * [ ] Captura un número entero del usuario.
    * [x] Captura una cadena siempre, incluso si el usuario escribe un número.
    * [ ] Captura un booleano dependiendo de la entrada.
    * [ ] Interrumpe el flujo de ejecución para validar tipos de datos.

11. ¿Qué característica define a una pila en programación?
    * [ ] Permite acceder a los elementos por su índice de posición.
    * [ ] Sigue el principio FIFO (First In, First Out).
    * [x] Sigue el principio LIFO (Last In, First Out).
    * [ ] Los elementos se eliminan desde el extremo denominado "front".

12. ¿Cuál de las siguientes operaciones no pertenece al manejo de una cola?
    * [ ] Enqueue
    * [ ] Peek
    * [x] Pop
    * [ ] Dequeue

13. ¿Cuál de estas afirmaciones sobre árboles binarios es verdadera?
    * [ ] Cada nodo puede tener hasta tres hijos.
    * [x] El recorrido en inorden visita primero el subárbol izquierdo, luego la raíz y finalmente el subárbol derecho.
    * [ ] En el recorrido en preorden, se visita primero el subárbol derecho, luego la raíz y finalmente el izquierdo.
    * [ ] Los árboles binarios no permiten búsquedas eficientes.

14. ¿Cuál es la principal diferencia entre una pila y una cola?
    * [ ] En una pila se eliminan elementos desde el "rear".
    * [ ] En una cola se añaden y eliminan elementos desde el mismo extremo.
    * [x] En una pila se añaden y eliminan desde el mismo extremo, mientras que en una cola se añaden en un extremo y se eliminan en el otro.
    * [ ] Las pilas y colas tienen el mismo comportamiento.

15. En una tabla hash, ¿para qué se utiliza una función de hash?
    * [ ] Para ordenar los valores en memoria.
    * [x] Para convertir una clave en un valor numérico y determinar su posición de almacenamiento.
    * [ ] Para asegurar que todos los elementos ocupen la misma posición.
    * [ ] Para eliminar duplicados automáticamente.

16. ¿Cuál de los siguientes recorridos de árbol binario devuelve los valores ordenados en un árbol binario de búsqueda?
    * [x] Inorden
    * [ ] Preorden
    * [ ] Postorden
    * [ ] Ninguno

17. Sobre el algoritmo de Dijkstra para encontrar caminos mínimos en grafos con pesos positivos, ¿cuál de estas afirmaciones es correcta?
    * [ ] Solo funciona con grafos no ponderados.
    * [x] Utiliza una cola de prioridad para determinar el próximo nodo a visitar.
    * [ ] Tiene complejidad constante O(1) para cualquier tamaño de grafo.
    * [ ] Modifica el grafo original durante su ejecución.

18. ¿Cuáles de estas operaciones están correctamente asociadas a sus estructuras de datos?
    * [x] Push — Pila
    * [x] Dequeue — Cola
    * [x] Preorden — Árbol binario
    * [ ] Hashing — Grafo

19. ¿Cuál es la definición correcta de complejidad espacial de un algoritmo?
    * [ ] Es la cantidad de pasos que tarda un algoritmo en ejecutarse.
    * [x] Es la cantidad de memoria necesaria para ejecutar un algoritmo.
    * [ ] Es la velocidad con la que crece la memoria utilizada al aumentar los datos.
    * [ ] Es la cantidad de memoria y tiempo combinados que consume un algoritmo.

20. ¿Cuál de las siguientes afirmaciones sobre notación Big O es verdadera?
    * [x] O(1) significa que el tiempo de ejecución es constante sin importar el tamaño de la entrada.
    * [ ] O(log n) significa que el tiempo de ejecución disminuye a medida que crece la entrada.
    * [ ] O(n²) significa que el tiempo de ejecución es independiente del tamaño de la entrada.
    * [ ] O(2^n) significa que el tiempo de ejecución crece linealmente con la entrada.

21. Dado el siguiente código: ¿Cuál es su complejidad temporal?
        ```py
        def algoritmo(n):
            for i in range(n):
                for j in range(n):
                    print(i, j)
        ```
    * [ ] O(n)
    * [x] O(n²)
    * [ ] O(log n)
    * [ ] O(1)

22. Según la regla de la multiplicación, si un algoritmo tiene dos bucles anidados donde cada uno recorre n elementos, ¿cuál es su complejidad?
    * [ ] O(n + n)
    * [x] O(n²)
    * [ ] O(2n)
    * [ ] O(1)

23. ¿Qué algoritmos tienen una complejidad de O(log n)?
    * [x] Búsqueda binaria
    * [ ] Ordenamiento de burbuja
    * [ ] Suma de los primeros n números con bucle
    * [ ] Todos los anteriores

24. ¿Cuál es el beneficio principal de un algoritmo de complejidad O(1) respecto a O(n)?
    * [ ] Consume menos memoria.
    * [x] Su tiempo de ejecución no varía con el tamaño de la entrada.
    * [ ] Puede manejar cualquier cantidad de datos.
    * [ ] Siempre es más eficiente que O(n log n).

25. Si un algoritmo consta de dos bloques consecutivos, uno O(n) y otro O(n²), según la regla de la suma, su complejidad total es:
    * [ ] O(n)
    * [x] O(n²)
    * [ ] O(2n²)
    * [ ] O(3n)

26. ¿Cuál es la definición de eficiencia algorítmica?
    * [ ] Cantidad mínima de recursos teóricos necesarios para resolver un problema.
    * [ ] Proporción entre el tiempo de ejecución y la cantidad de memoria disponible.
    * [x] Medida de los recursos consumidos por un algoritmo, como tiempo y memoria.
    * [ ] Número de líneas de código que utiliza un algoritmo.

27. Sobre el ordenamiento burbuja implementado en Python:
    * [ ] Tiene complejidad O(n log n)
    * [ ] Es más eficiente que la búsqueda binaria
    * [x] Tiene complejidad O(n²)
    * [ ] Es un algoritmo de ordenamiento logarítmico

28. ¿Cuáles de las siguientes afirmaciones son verdaderas?
    * [ ] Un algoritmo O(1) siempre es más rápido que uno O(n) para cualquier tamaño de entrada.
    * [x] La búsqueda binaria requiere que los datos estén ordenados.
    * [ ] O(n²) crece más rápido que O(n²) a medida que n aumenta.
    * [x] O(log n) crece más lento que O(n²) a medida que n aumenta.

29. ¿Cuál de las siguientes definiciones describe mejor a una clase en Python?
    * [ ] Es una instancia de un objeto que contiene métodos y atributos.
    * [x] Es una plantilla para crear objetos, que define atributos y métodos comunes.
    * [ ] Es una variable que almacena una secuencia de valores.
    * [ ] Es un tipo de función que no admite parámetros.

30. ¿Qué es un objeto en Python?
    * [ ] Es una copia exacta de otra clase.
    * [x] Es una instancia concreta creada a partir de una clase.
    * [ ] Es un método que pertenece solo a las subclases.
    * [ ] Es un tipo especial de atributo de clase.

31. ¿Cuál es la función del método especial __init__ en Python?  
    * [x] Inicializa los atributos de una clase y se ejecuta automáticamente al crear una instancia.
    * [ ] Destruye una instancia antes de finalizar el programa.
    * [ ] Retorna una representación en cadena del objeto.
    * [ ] Es un método opcional que agrega métodos a una clase.

32. ¿Qué afirmación sobre atributos de instancia y atributos de clase es correcta?  
    * [ ] Los atributos de instancia son compartidos por todas las instancias de una clase.
    * [ ] Los atributos de clase solo existen dentro de los métodos de instancia.
    * [x] Los atributos de instancia pertenecen a cada objeto creado y pueden tener valores diferentes.
    * [ ] Los atributos de clase se declaran dentro de __init__.

33. ¿Cuál de estas opciones define correctamente el concepto de herencia en POO?  
    * [x] Proceso por el cual una clase hereda atributos y métodos de otra.
    * [ ] Proceso para asignar valores por defecto a los atributos.
    * [ ] Definir métodos con el mismo nombre en clases no relacionadas.
    * [ ] Crear una instancia de una clase a partir de otra.

34. ¿Cuál es el objetivo del método especial __str__ en una clase de Python?  
    * [x] Retornar una representación legible en cadena del objeto.
    * [ ] Inicializar atributos cuando se crea la clase.
    * [ ] Cambiar la dirección de memoria del objeto.
    * [ ] Ejecutar automáticamente una operación de ordenamiento.

35. ¿Cuáles de los siguientes principios forman parte de la Programación Orientada a Objetos?  
    * [x] Encapsulamiento
    * [ ] Recursividad
    * [x] Herencia
    * [ ] Secuencialidad
