# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("----------breadth_first----------")
print(search.breadth_first_graph_search(ab).path())
print("----------depth_first----------")
print(search.depth_first_graph_search(ab).path())
print("----------branch_and_bound----------")
print(search.branch_and_bound_graph_search(ab).path())
print("----------informed_branch_and_bound----------")
print(search.informed_branch_and_bound_graph_search(ab).path())


# Result:
# ----------breadth_first----------
# Nodos visitados = 16
# Nodos expandidos = 8
# [<Node B>, <Node F>, <Node S>, <Node A>]
# ----------depth_first----------
# Nodos visitados = 10
# Nodos expandidos = 7
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]
# ----------branch_and_bound----------
# Nodos visitados = 24
# Nodos expandidos = 12
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
# ----------informed_branch_and_bound----------
# Nodos visitados = 6
# Nodos expandidos = 5
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
