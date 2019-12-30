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

## BFS with two lists (from AOC 2018 day 22)

Personally, I like to implement BFS using a pair of lists instead of a queue:

```python
current = [start]    # nodes with cost=n
next = []            # nodes with cost=n+1

while current:
    for node in current:
        next.extend(successors(node))
    current, next = next, []

```

This is essentially the same as using a single queue, performance-wise; it allows you to easily keep track of the current level (by incrementing a counter on each iteration of the while loop); and it makes it a bit more obvious that you're assuming all nodes in "next" to have the same cost.

## Advent of Code implementation

Used BFS in the AoC 2018 challenge for day 15 - elves vs goblins, and in the AoC 2019 challenge for day 15 (again!!!) (directing a droid through a maze using the `intcode` machine)

### AoC 2019 day 15 implementation

This is a really short implementation, can be easily re-used.

It requires a graph (dictionary of lists) with valid neighbors - can be generated when mapping out a maze.

```python
graph = defaultdict(list)

    # generate neighbors in the graph when mapping out the maze - only add accessible cells
    # in a loop:
    graph[current_pos].append(next_pos)
    graph[next_pos].append(current_pos)
   
```

```python
# Do a BFS using the graph, starting from the oxygen source
# - valid neighbors are contained in the graph dictionary

q = deque([(start_pos, [])])
seen = set()
path = defaultdict(list)

while(q):
    current_pos, current_path = q.pop()

    # go through neighbors using the graph
    for neighbor in graph[current_pos]:
        if neighbor not in seen:
            seen.add(neighbor)
            path[neighbor] = current_path + [neighbor]
            q.appendleft((neighbor, current_path + [neighbor]))

logging.info('BFS ended!')

# get the longest path length from the starting node
longest_from_start = max(path, key=lambda x: len(path[x]))    
```

## TO DO

* How to deal with cyclical graphs (where there are more than one path to some nodes) - currently we take the first path