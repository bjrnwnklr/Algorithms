# Topological sort

In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another; in this application, a topological ordering is just a valid sequence for the tasks. A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph (DAG). Any DAG has at least one topological ordering, and algorithms are known for constructing a topological ordering of any DAG in linear time.

## Reading / explanations

[Topological sorting (Wikipedia)](https://en.m.wikipedia.org/wiki/Topological_sorting)

[MSDN blog explaining topological sort in JS](https://blogs.msdn.microsoft.com/ericlippert/2004/03/16/im-putting-on-my-top-hat-tying-up-my-white-tie-brushing-out-my-tails-in-that-order/)

[Topological sort using DFS (github)](https://gist.github.com/kachayev/5910538)

## Algorithm

Wikipedia has a good explanation and pseudo-code that I used for the AoC 2018 day 7 solution.

### Kahn's algorithm	

One of these algorithms, first described by Kahn (1962), works by choosing vertices in the same order as the eventual topological sort.

First, find a list of "start nodes" which have no incoming edges and insert them into a set S; at least one such node must exist in a non-empty acyclic graph. Then:

```
L ← Empty list that will contain the sorted elements
S ← Set of all nodes with no incoming edge
while S is non-empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S
if graph has edges then
    return error   (graph has at least one cycle)
else 
    return L   (a topologically sorted order)
```

If the graph is a DAG, a solution will be contained in the list L (the solution is not necessarily unique). Otherwise, the graph must have at least one cycle and therefore a topological sorting is impossible.

Reflecting the non-uniqueness of the resulting sort, the structure S can be simply a set or a queue or a stack. Depending on the order that nodes n are removed from set S, a different solution is created. A variation of Kahn's algorithm that breaks ties lexicographically forms a key component of the Coffman–Graham algorithm for parallel scheduling and layered graph drawing.

## Implementation

Day 7 of Advent of Code 2018 can be solved using topological sorting. See relevant code:

```python
from collections import defaultdict
import heapq

result = []
instr = defaultdict(list)
dep = defaultdict(list)

with open(r'input1.txt') as f:
    for l in f:
        x = l.split(' ')
        instr[x[1]].append(x[7])
        dep[x[7]].append(x[1])

# find all starting values that don't have dependencies
s = [x for x in instr if x not in dep]

# topological sort with a heapq for alphabetical order
while s:
    # pick next element without any dependencies
    cur = heapq.heappop(s)
    # and add it to the results
    result.append(cur)

    # now take next node which depends on current element
    for m in instr[cur]:
        # and remove the edge from cur to m
        dep[m].remove(cur)
        # if m has no more incoming edges (all dependencies fulfilled),
        # add it to the heapq
        if not dep[m]:
            heapq.heappush(s, m)

print(''.join(result))
```

## Using networkX library

networkX has an implementation of topological sort built in:

```python
import networkx as nx

def solve(lines):
    G = nx.DiGraph()
    for line in lines:
        parts = line.split(" ")
        G.add_edge(parts[1], parts[7])
    print(''.join(nx.lexicographical_topological_sort(G)))
```