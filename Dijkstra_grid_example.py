from collections import defaultdict
from heapq import heappush, heappop
import random

# generate a simple grid with each node in the grid having one of 
# three terrain types (0, 1, 2) - which is also used to generate 
# the weight of the edges:
#   - each step costs minimum of 1
#   - changing between terrain additionally costs abs(a - b)
GRID_SIZE = 20
start = (0, 0)
target = (19, 19)
TYPES = 3
types = {0: '.', 1: '~', 2: '#'}
n_coords = [(0, -1), (1, 0), (0, 1), (-1, 0)]

#grid = {(c, r): random.randrange(0, TYPES) for c in range(GRID_SIZE) for r in range(GRID_SIZE)}
def read_grid():
    g = dict()
    for r, l in enumerate(open('grid.txt')):
        for c, x in enumerate(l.rstrip()):
            g[(c, r)] = int(x)
    return g

def print_grid(grid):
    for r in range(GRID_SIZE):
        print(''.join([types[grid[(c, r)]] for c in range(GRID_SIZE)]))

def write_grid(grid):
    f = open('grid.txt', 'w')
    for r in range(GRID_SIZE):
        f.write(''.join([str(grid[(c, r)]) for c in range(GRID_SIZE)]) + '\n')
    f.close


def dijkstra(grid, f, t):

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path += (v1, )
            if v1 == t: return (cost, path)

            # generate cost for neighbours and 
            # add them to a list
            for n in n_coords:
                v_next = (v1[0] + n[0], v1[1] + n[1])
                if v_next in grid and v_next not in seen:
                    c = 1 + abs(grid[v1] - grid[v_next])
                    heappush(q, (cost + c, v_next, path))

    return float("inf")
