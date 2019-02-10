# Breadth First Search (BFS)

Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

It uses the opposite strategy as depth-first search, which instead explores the highest-depth nodes first before being forced to backtrack and expand shallower nodes.

BFS can be implemented using a queue (First in first out).

If all the edges in a graph are of the same weight, then BFS can also be used to find the minimum distance between the nodes in a graph.

### Complexity

The time complexity of BFS is O(V + E), where V is the number of nodes and E is the number of edges.

## Explanations / Examples

[Wikipedia - BFS](https://en.wikipedia.org/wiki/Breadth-first_search)

[Breaking Down Breadth-First Search (medium basecs)](https://medium.com/basecs/breaking-down-breadth-first-search-cebe696709d9)

[Hackerearth - BFS notes and tutorial](https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/)

[Finding Shortest Paths using Breadth First Search (medium freecodecamp)](https://medium.freecodecamp.org/exploring-the-applications-and-limits-of-breadth-first-search-to-the-shortest-paths-in-a-weighted-1e7b28b3307)
This is a very detailed description, covering many scenarios, e.g. in weighted graphs, level traversal, finding shortest path for a maximum number of levels.

## My clean implementation

This uses a grid generated from walls (type: 1) and floor (type: 0), then generates a start and target coordinate.

The BFS algorithm calculates paths to each accessible square from `start` and returns a `defaultdict` with the paths. The length of the respective dictionary entry is the number of steps required to get to the respective tile.

```python
############## BFS algorithm
# returns a dictionary of paths from start to each accessible square in the grid
def BFS(grid, start):
    q = deque([(start, [])])
    seen = set()
    path = defaultdict(list)
    while q:
        v1, p = q.pop() # removes element from the right side of the queue
        if v1 not in seen:
            seen.add(v1)
            
            # find all valid neighbours
            for n in n_coords:
                v_next = (v1[0] + n[0], v1[1] + n[1])
                if (v_next in grid 
                    and v_next not in seen 
                    and v_next not in path
                    and grid[v_next] != 1):
                    # push into queue - on the left side
                    # set the path to this new square
                    path[v_next] = p + [v_next]
                    q.appendleft((v_next, p + [v_next]))
                  
    # once q is empty, return the dictionary with paths
    return path
```

## Advent of Code implementation

Used BFS in the AoC 2018 challenge for day 15 - elves vs goblins

