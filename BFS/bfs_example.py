from collections import defaultdict
from heapq import heappush, heappop
import random

# generate a simple grid with each node in the grid having one of 
# two terrain types (0 - accessible, 1 - wall, inaccessible). Each step costs 1, 
# walls are inaccessible.
GRID_SIZE = 20
TYPES = 2
types = {0: '.', 1: '#'}
n_coords = [(0, -1), (1, 0), (0, 1), (-1, 0)] # coordinates of neighbours


################### Helper functions

def gen_grid():
    #grid = {(c, r): random.randrange(0, TYPES) for c in range(GRID_SIZE) for r in range(GRID_SIZE)}
    grid = {(c, r): 1 if c == 0 or r == 0 or c == GRID_SIZE - 1 or r == GRID_SIZE - 1 else 0 
            for c in range(GRID_SIZE) for r in range(GRID_SIZE)}
    for r in range(1, GRID_SIZE - 1):
        for c in range(1, GRID_SIZE - 1):
            grid[(c, r)] = random.choices([0, 1], cum_weights = [85, 100])[0]
    return grid

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

def print_path(grid, path, start, target):
    for r in range(GRID_SIZE):
        line = ''
        for c in range(GRID_SIZE):
            if (c, r) == start:
                x = 'S'
            elif (c, r) == target:
                x = 'T'
            elif (c, r) in path:
                x = 'o'
            else:
                x = types[grid[(c, r)]]
            line += x
        print(line)

def rand_select(grid):
    while True:
        c, r = random.randrange(1, GRID_SIZE - 1), random.randrange(1, GRID_SIZE - 1)
        if grid[(c, r)] == 0: return (c, r)


############ run an example
def run_example():
    grid = gen_grid()
    print_grid(grid)
    # pick start and target coordinates
    start = rand_select(grid)
    target = rand_select(grid)
    p = []
    #c, p = dijkstra(grid, start, target)
    #print(c, p)
    print_path(grid, p, start, target)

############## BFS algorithm
# returns ?
def BFS(grid, start):
    q = [start]
    seen = set()
    path = defaultdict(list)
    while q:
        v1 = q.pop()
        if v1 not in seen:
            seen.add(v1)
            path[v1].append(v1)

            # find all valid neighbours
            for n in n_coords:
                v_next = (v1[0] + n[0], v1[1] + n[1])
                if v_next in grid and v_next not in seen and grid[v_next] != 1:
                    # push into queue
                    # mark as seen