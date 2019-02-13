# Depth First Search (DFS)

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

DFS can be used to find a path through a maze. It will find if there is a path, but not necessarily the shortest path.

### Complexity

The time complexity of DFS is O(V + E), where V is the number of nodes and E is the number of edges.

## Explanations / Examples

[Depth First Search - Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)

[Demystifying Depth First Search - medium basecs](https://medium.com/basecs/demystifying-depth-first-search-a7c14cccf056)

## Example implementation

See `dfs_example.py` for a clean example in a maze.

Maze generated from [Maze generator](http://www.delorie.com/game-room/mazes/genmaze.cgi).

```python
def DFS(grid, dims, start, target):

    stack = deque([(start, [start])])

    while stack:
        v, path = stack.pop()
        
        for n in n_coords:
            v_next = (v[0] + n[0], v[1] + n[1])
            # end if we found the target position
            if v_next == target:
                return path + [target]
            # else put all valid and not visited neighbour vertices onto the stack
            elif (v_next in grid 
                and v_next not in path 
                and grid[v_next] != 1):
                stack.append((v_next, path + [v_next]))
    # return None if we didn't find a path to the target
    return None
```
