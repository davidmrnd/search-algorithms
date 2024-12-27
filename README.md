# Algoritmos de Búsqueda

Este repositorio implementa varios algoritmos de búsqueda, tanto informados como no informados, utilizados para resolver problemas de búsqueda en grafos. A continuación se describen los algoritmos implementados, junto con su clasificación y una breve explicación de su funcionamiento.

## Algoritmos Implementados

### 1. **Búsqueda en Amplitud (Breadth-First Search - BFS)**

#### Descripción:
El algoritmo de búsqueda en amplitud explora los nodos de un grafo nivel por nivel, comenzando desde el nodo inicial. Visita primero todos los nodos a una distancia de un solo paso, luego los nodos a dos pasos, y así sucesivamente, hasta encontrar el objetivo.

#### Propiedad:
- **No informado**: No utiliza ninguna información adicional más allá de la estructura del grafo. No tiene una función heurística.

#### Implementación:
```python
def breadth_first_graph_search(problem):
    # Busca los nodos más superficiales en el árbol de búsqueda primero
    return graph_search(problem, FIFOQueue())  # FIFOQueue -> fringe
```

### 2. **Búsqueda en Profundidad (Depth-First Search - DFS)**

#### Descripción:
La búsqueda en profundidad explora tan profundamente como sea posible cada rama antes de retroceder. Empuja los nodos en una pila y sigue explorando hasta que llega al final de una rama, luego retrocede y explora la siguiente.

#### Propiedad:
- **No informado**: Similar a la búsqueda en amplitud, no utiliza ninguna información heurística y solo se basa en la estructura del grafo.

#### Implementación:
```python
def depth_first_graph_search(problem):
    # Busca los nodos más profundos en el árbol de búsqueda primero
    return graph_search(problem, Stack())  # Stack -> fringe
```

### 3. **Búsqueda por Rama y Poda (Branch and Bound Search)**

#### Descripción:
Este algoritmo realiza una búsqueda similar a la de amplitud, pero con la ventaja de que mantiene una lista de los nodos en función de su costo de camino. En cada paso, expande el nodo con el costo más bajo.

#### Propiedad:
- **No informado**: Aunque intenta optimizar el camino, sigue sin utilizar heurísticas y solo se enfoca en los costos de los caminos.

#### Implementación:
```python
def branch_and_bound_graph_search(problem):
    # Busca los nodos más superficiales primero, asegurando que se encuentre el camino más corto en un árbol de búsqueda no ponderado.
    return graph_search(problem, BranchAndBoundQueue())  # BranchAndBoundQueue -> fringe
```

### 4. **Búsqueda por Rama y Poda Informada (Informed Branch and Bound Search)**

#### Descripción:
Este algoritmo combina la búsqueda por rama y poda con una función heurística que estima el costo de alcanzar el objetivo. Utiliza la suma del costo del camino y la heurística para decidir qué nodo expandir a continuación, guiando la búsqueda hacia los nodos más prometedores.

#### Propiedad:
- **Informado**: Utiliza una función heurística para guiar la búsqueda, lo que mejora la eficiencia en comparación con los algoritmos no informados.

#### Implementación:
```python
def informed_branch_and_bound_graph_search(problem):
    # Busca los nodos en función de la suma del costo del camino y la estimación heurística al objetivo, guiando la búsqueda hacia los caminos más prometedores.
    return graph_search(problem, InformedBranchAndBoundQueue(problem))  # InformedBranchAndBoundQueue -> fringe
```

## Descripción de Clases y Funciones

### Clase `Queue`

Es una clase abstracta que define los métodos comunes para las estructuras de datos utilizadas en los algoritmos de búsqueda, como la pila (Stack), la cola (FIFOQueue), y las colas con prioridad (BranchAndBoundQueue, InformedBranchAndBoundQueue).

### Funciones de Búsqueda

- **`graph_search(problem, fringe)`**: Función central que realiza la búsqueda a través de los sucesores del problema utilizando la cola proporcionada (`fringe`). Esta función se utiliza en todos los algoritmos de búsqueda.

### Estructuras de Datos

- **`Stack()`**: Implementa una pila (LIFO - Last In, First Out).
- **`FIFOQueue()`**: Implementa una cola (FIFO - First In, First Out).
- **`BranchAndBoundQueue()`**: Implementa una cola con prioridad, que ordena los nodos por el costo del camino.
- **`InformedBranchAndBoundQueue()`**: Similar a `BranchAndBoundQueue`, pero también utiliza una función heurística para ordenar los nodos según el costo total estimado (costo del camino + heurística).

## Ejemplo de Uso

El siguiente ejemplo muestra cómo utilizar los algoritmos de búsqueda implementados para resolver un problema de búsqueda en un grafo. En este caso, el problema es encontrar un camino entre dos ciudades en el mapa de Rumanía.

```python
import search

ab = search.GPSProblem('A', 'B', search.romania)

print("----------breadth_first----------")
print(search.breadth_first_graph_search(ab).path())

print("----------depth_first----------")
print(search.depth_first_graph_search(ab).path())

print("----------branch_and_bound----------")
print(search.branch_and_bound_graph_search(ab).path())

print("----------informed_branch_and_bound----------")
print(search.informed_branch_and_bound_graph_search(ab).path())
```

### Resultado Esperado

```text
----------breadth_first----------
Nodos visitados = 16
Nodos expandidos = 8
[<Node B>, <Node F>, <Node S>, <Node A>]

----------depth_first----------
Nodos visitados = 10
Nodos expandidos = 7
[<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]

----------branch_and_bound----------
Nodos visitados = 24
Nodos expandidos = 12
[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]

----------informed_branch_and_bound----------
Nodos visitados = 6
Nodos expandidos = 5
[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
```

## Conclusión

En este repositorio se presentan diversos algoritmos de búsqueda aplicados a problemas de grafos. Los algoritmos de búsqueda en amplitud y profundidad son enfoques no informados que exploran los nodos del grafo sin utilizar ninguna información adicional, garantizando encontrar una solución, pero con eficiencia variable. Por otro lado, los algoritmos de búsqueda por rama y poda, tanto informados como no informados, permiten una búsqueda más eficiente al organizar y priorizar la exploración de nodos. En particular, la búsqueda informada, al utilizar una función heurística, dirige la exploración hacia las soluciones más prometedoras, mejorando significativamente el rendimiento en comparación con los métodos tradicionales no informados.
