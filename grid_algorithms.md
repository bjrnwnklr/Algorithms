# Grid pathfinding algorithms

Summary of search algorithms for finding paths in grids...

[Grid pathfinding optimizations](https://www.redblobgames.com/pathfinding/grids/algorithms.html)

[Grids and Graphs](https://www.redblobgames.com/pathfinding/grids/graphs.html)

[Fast pathfinding via symmetry](http://aigamedev.com/open/tutorial/symmetry-in-pathfinding/)

[Map representations](http://theory.stanford.edu/~amitp/GameProgramming/MapRepresentations.html)

## Comparison between commonly used algorithms

### 1) Breadth first search (BFS)

Breadth First Search explores equally in all directions. This is an incredibly useful algorithm, not only for regular path finding, but also for procedural map generation, flow field pathfinding, distance maps, and other types of map analysis.

Characteristic: uses a **queue** (FIFO)

### 2) Depth first search (DFS)

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

Characteristic: uses a **stack** (LIFO)

* useful to determine _IF_ there is a valid path to a target in a maze. It will determine if a path exists, but not necessarily the shortest one
* _NOT EFFICIENT_ if there are wide open spaces e.g. in a grid. It spends a lot of time backtracking until it has visited all nodes. Use BFS or A* for such cases.

### 3) Dijkstra

Dijkstra’s Algorithm (also called Uniform Cost Search) lets us prioritize which paths to explore. Instead of exploring all possible paths equally, it favors lower cost paths. We can assign lower costs to encourage moving on roads, higher costs to avoid forests, higher costs to discourage going near enemies, and more. When movement costs vary, we use this instead of Breadth First Search.

Characteristic: uses a **priority queue** (priority sorted FIFO)

### 4) A*

A* is a modification of Dijkstra’s Algorithm that is optimized for a single destination. Dijkstra’s Algorithm can find paths to all locations; A* finds paths to one location, or the closest of several locations. It prioritizes paths that seem to be leading closer to a goal.

Characteristic: uses a **priority queue with added heuristic estimation** (priority sorted FIFO)

[A* implementation](https://www.redblobgames.com/pathfinding/a-star/implementation.html)

### 5) Jump Point Search
   
Jump Point Search (JPS) [3] is an online symmetry breaking algorithm which speeds up pathfinding on uniform-cost grid maps by "jumping over" many locations that would otherwise need to be explicitly considered. Unlike other similar algorithms JPS requires no preprocessing and has no memory overheads. Further, it is easily combined with most existing speedup techniques -- including abstraction and memory heuristics. It can speed up A* search by over an order magnitude and more.

### 6) Flood fill algorithms

[Wikipedia: Flood fill](https://en.wikipedia.org/wiki/Flood_fill)

Flood fill, also called seed fill, is an algorithm that determines the area connected to a given node in a multi-dimensional array. It is used in the "bucket" fill tool of paint programs to fill connected, similarly-colored areas with a different color, and in games such as Go and Minesweeper for determining which pieces are cleared.

The flood-fill algorithm takes three parameters: a start node, a target color, and a replacement color. The algorithm looks for all nodes in the array that are connected to the start node by a path of the target color and changes them to the replacement color. There are many ways in which the flood-fill algorithm can be structured, but they all make use of a queue or stack data structure, explicitly or implicitly.

Depending on whether we consider nodes touching at the corners connected or not, we have two variations: eight-way and four-way respectively.

Characteristic: uses a **queue** (FIFO) (very similar to BFS)
