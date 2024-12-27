# Estrategias de Búsqueda Ramificación y Acotación

## **Introducción**
El objetivo de esta práctica es implementar y analizar dos estrategias de búsqueda en grafos:

1. **Ramificación y acotación** (búsqueda no informada).
2. **Ramificación y acotación con subestimación** (búsqueda informada con heurística).

Ambos métodos se probarán sobre el problema del grafo de las ciudades de Rumanía. Además, se comparará la eficiencia de estas estrategias en términos del número de nodos expandidos con respecto a los métodos de búsqueda primero en anchura y primero en profundidad.

---

## **1. Búsqueda No Informada: Ramificación y Acotación con Búsqueda No Informada**
En la primera parte del código se presentan dos funciones de búsqueda no informada: búsqueda en anchura (breadth-first search) y búsqueda en profundidad (depth-first search). Ambas siguen el esquema básico de búsqueda "graph_search", que se encarga de explorar los nodos del espacio de soluciones sin ninguna forma de priorización basada en heurísticas.

### **Función breadth_first_graph_search (Búsqueda en anchura)**
La búsqueda en anchura sigue la estrategia FIFO, lo que significa que los nodos más cercanos a la raíz del árbol de búsqueda se exploran primero. Esta estrategia garantiza encontrar la solución óptima en un árbol no ponderado, pero puede ser muy ineficiente en términos de tiempo y memoria cuando el espacio de búsqueda es grande.

### **Función depth_first_graph_search (Búsqueda en profundidad)**
Por otro lado, la búsqueda en profundidad explora los nodos más profundos del árbol de búsqueda primero, lo que permite una exploración más agresiva de los nodos descendientes antes de retroceder. Aunque esta estrategia no garantiza encontrar la solución óptima, es más eficiente en términos de memoria, ya que solo necesita almacenar los nodos en la ruta actual.

Ambas funciones (breadth_first_graph_search y depth_first_graph_search) son ejemplos de búsqueda no informada. El principal inconveniente de estas técnicas es su ineficiencia cuando el espacio de búsqueda es grande o infinito, ya que no aprovechan ninguna heurística para guiar la exploración.

## **2. Búsqueda Informada con Heurística: Ramificación y Acotación con Subestimación**
En la segunda parte del código, se muestran dos funciones que emplean búsqueda informada con heurísticas: ramificación y acotación con subestimación. Estas técnicas utilizan una función heurística para priorizar la expansión de ciertos nodos, guiando la búsqueda hacia las áreas más prometedoras del espacio de soluciones.

### **Función branch_and_bound_graph_search**
Esta función implementa una variante de la búsqueda de ramificación y acotación. Utiliza una estrategia basada en la subestimación del costo para determinar qué nodos explorar a continuación. En lugar de explorar todos los nodos por igual, esta técnica prioriza aquellos que tienen un costo total más bajo, garantizando que la solución óptima se encuentre de manera eficiente.
El algoritmo expande los nodos en función de su costo estimado. Los nodos con un costo total (coste del camino más el costo estimado hacia el objetivo) menor se exploran primero, lo que mejora significativamente la eficiencia en comparación con las búsquedas no informadas.

### **Función informed_branch_and_bound_graph_search**
La búsqueda informada de ramificación y acotación mejora aún más el proceso utilizando una heurística que estima la distancia al objetivo. En este caso, se suman el costo acumulado del camino y la estimación de la heurística para determinar qué nodos son más prometedores. Esta técnica permite guiar la búsqueda hacia las áreas con mayor probabilidad de encontrar la solución óptima rápidamente.
El algoritmo prioriza los nodos que tienen el costo total más bajo, sumando el costo hasta el nodo actual y la estimación de la heurística hacia el objetivo. Esto mejora la eficiencia al reducir el número de nodos explorados y acelera la convergencia hacia la solución.

---

## **Decisiones de Diseño**
1. **Tamaño de las Imágenes**:
   - Las imágenes se redimensionaron a \(128 x 128\) píxeles.
   - **Motivo**: Asegurar uniformidad en la entrada al modelo y equilibrar detalle visual con eficiencia computacional.

2. **Normalización**:
   - Los valores de píxeles fueron normalizados a \([-1, 1]\).
   - **Motivo**: Mejorar la convergencia del entrenamiento.

3. **Filtros y Capas**:
   - Se utilizaron 16 y 32 filtros en las capas convolucionales.
   - **Motivo**: Extraer características representativas sin saturar la capacidad computacional.

4. **Función de Pérdida**:
   - Se empleó `CrossEntropyLoss`.
   - **Motivo**: Es ideal para problemas de clasificación multiclase.

5. **Optimizador**:
   - Se utilizó Adam con una tasa de aprendizaje inicial de 0.001.
   - **Motivo**: Adam es robusto, dinámico y eficiente en términos de tiempo de convergencia.

---

## **Conclusión**
Las funciones de búsqueda no informada (breadth_first_graph_search y depth_first_graph_search) son sencillas de implementar y garantizan una solución óptima en ciertos contextos, pero pueden ser ineficaces cuando el espacio de búsqueda es grande o infinito. Por otro lado, las funciones de búsqueda informada con heurísticas (branch_and_bound_graph_search y informed_branch_and_bound_graph_search) mejoran significativamente la eficiencia al guiar la búsqueda hacia las soluciones más prometedoras. Estas estrategias informadas son más rápidas y eficientes, pero dependen de la calidad de la heurística para asegurar la calidad de la solución. En resumen, la incorporación de heurísticas mejora drásticamente el rendimiento en la resolución de problemas de optimización.

---

## **Aspectos Teóricos**
1. **Búsquedas No Informadas**:
   - En espacios grandes, pueden ser muy ineficientes debido a la explosión combinatoria.

2. **Búsquedas Informadas**:
   - Reducción de nodos explorados al guiarse por la heurística, mejorando el tiempo y espacio de ejecución.

3. **Heurísticas Fuertes**:
   - Mejoran significativamente la eficiencia y reducen el tiempo de búsqueda.

4. **Heurísticas Débiles**:
   - Afectan negativamente la eficiencia y acercan la búsqueda a una no informada.

---

Este proyecto demuestra que las búsquedas informadas, al usar heurísticas, son más eficientes que las no informadas, aunque dependen de la calidad de la heurística. Las búsquedas no informadas garantizan soluciones óptimas, pero con mayor costo computacional.
