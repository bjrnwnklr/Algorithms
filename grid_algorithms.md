# Grid pathfinding algorithms

Summary of search algorithms for finding paths in grids...

[Grid pathfinding optimizations](https://www.redblobgames.com/pathfinding/grids/algorithms.html)

[Grids and Graphs](https://www.redblobgames.com/pathfinding/grids/graphs.html)

[Fast pathfinding via symmetry](http://aigamedev.com/open/tutorial/symmetry-in-pathfinding/)

[Map representations](http://theory.stanford.edu/~amitp/GameProgramming/MapRepresentations.html)

## Comparison between commonly used algorithms

### 1) Breadth first search (BFS)

Breadth First Search explores equally in all directions. This is an incredibly useful algorithm, not only for regular path finding, but also for procedural map generation, flow field pathfinding, distance maps, and other types of map analysis.

### 2) Depth first search (DFS)

### 3) Dijkstra

Dijkstra’s Algorithm (also called Uniform Cost Search) lets us prioritize which paths to explore. Instead of exploring all possible paths equally, it favors lower cost paths. We can assign lower costs to encourage moving on roads, higher costs to avoid forests, higher costs to discourage going near enemies, and more. When movement costs vary, we use this instead of Breadth First Search.

### 4) A*

A* is a modification of Dijkstra’s Algorithm that is optimized for a single destination. Dijkstra’s Algorithm can find paths to all locations; A* finds paths to one location, or the closest of several locations. It prioritizes paths that seem to be leading closer to a goal.

[A* implementation](https://www.redblobgames.com/pathfinding/a-star/implementation.html)

### 5) Jump Point Search
   
Jump Point Search (JPS) [3] is an online symmetry breaking algorithm which speeds up pathfinding on uniform-cost grid maps by "jumping over" many locations that would otherwise need to be explicitly considered. Unlike other similar algorithms JPS requires no preprocessing and has no memory overheads. Further, it is easily combined with most existing speedup techniques -- including abstraction and memory heuristics. It can speed up A* search by over an order magnitude and more.

### 6) Flood fill algorithms

[Wikipedia: Flood fill](https://en.wikipedia.org/wiki/Flood_fill)
