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

## Implementing Dijkstra to find shortest path in a grid

Advent of code 2018, day 22, part 2 - solved using Dijkstra search with 3 dimensions (row, columns, tool equipped).

## AOC 2019, day 18

```python
# Dijkstra stuff
# q contains the following:
# 0: length of steps
# 1: current position (key, key bitmap) tuple
# 2: current path (list of keys)
keywalk_start = ('@', start_key_mask)
q = [(0, keywalk_start, ())]
seen = set()
endstates = []
distance_to = defaultdict(lambda: 1e09)

while q:
    (current_steps, current_pos, current_path) = heappop(q)
    logging.debug('Dijkstra: popped {}, {}, {} from heapq.'.format(current_steps, current_pos, current_path))
    if current_pos not in seen:
        seen.add(current_pos)
        current_path += (current_pos, )

        # check if we reached the end
        if current_pos[1] == full_keys:
            endstates.append((current_steps, current_path))
            continue

        for next_step in reachable_keys(key_graph, current_pos):
            # get number of steps to next_step step count
            add_steps = [s for k, s, _ in key_graph[current_pos[0]] if k == next_step[0]][0]

            # check if we found a key and modify the key_mask
            if next_step[0] in key_positions:
                key_mask = set_bit(next_step[1], key_bits[next_step[0]])
                logging.debug('Picked up key {} and updated bitmask to {}'.format(next_step[0], key_mask))
            else:
                key_mask = next_step[1]

            if next_step not in seen and current_steps + add_steps < distance_to[(next_step[0], key_mask)]: ##### record distance per state and compare if we found a shorter state (only then push onto queue)
                distance_to[(next_step[0], key_mask)] = current_steps + add_steps
                heappush(q, (current_steps + add_steps, (next_step[0], key_mask), current_path))

```

## Graphs using networkx / nx.Graph

The NetworkX library for Python provides a Graph model and many different search algorithms, including Dijkstra.

[NetworkX tutorial](https://networkx.github.io/documentation/stable/tutorial.html)

## Dijkstra or other search algorithms (BFS etc) with multiple states

**IMPORTANT** If we are using any of the search algorithms to find the shortest path to a position (e.g. in a 2d grid), but have multiple other parameters that define a state in the search tree (e.g. number of steps taken, a key configuration, etc) that allow us to reach the position in the 2d grid, we need to be aware that the first instance of when we reach the targetted end position might not be the shortest path yet.

How to find the shortest path in these situations:

-   Record the shortest path for each instance of reaching the target position (as there might be multiple states we can reach the end position in / from - depending on the other parameters of the state), and then after the queue is empty, take the minimum of these final end states.
-   Build in a check using a dictionary that records the shortest length taken to reach a given state, and discard any next steps / neighbors if they have a shorter distance to the same state. This is an optimization that also cuts down on the number of states being evaluated.

AOC 2023 day 17 uses Dijkstra with 2 other constraints (number of steps taken straight ahead, direction) and uses an additional dictionary (which can also be used instead of the seen set) to discard any states that have a longer path to a given state.
