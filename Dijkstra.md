# Dijkstra search algorithm

Dijkstra is a search algorithm that can be used for graphs with weighted edges to find the shortest path between nodes, e.g. for the shortest route between cities (or nodes in a grid, e.g. a labyrinth).

One of the benefits of the algorithm is that it generates a map of the shortest distance from a source node to every other node in the graph - which can then be queried multiple times without recalculating.

## Understanding the Dijkstra algorithm

[Finding the shortest path with a little help from Dijkstra](https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e)

## Clean Dijkstra implementation

[Dijkstra in Python using a heapq](https://gist.github.com/kryptek/b12775509abf86f90c3078ae88d9538b)

```python
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path += (v1, )
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print("=== Dijkstra ===")
    print(edges)
    print("A -> E:")
    print(dijkstra(edges, "A", "E"))
    print("F -> G:")
    print(dijkstra(edges, "F", "G"))
```

## Graphs using networkx / nx.Graph

The NetworkX library for Python provides a Graph model and many different search algorithms, including Dijkstra.

[NetworkX tutorial](https://networkx.github.io/documentation/stable/tutorial.html)
