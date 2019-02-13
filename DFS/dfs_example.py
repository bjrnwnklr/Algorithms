from collections import defaultdict, deque
import random

# generate a simple grid with each node in the grid having one of 
# two terrain types (0 - accessible, 1 - wall, inaccessible). Each step costs 1, 
# walls are inaccessible.
TYPES = 2
start = (0, 1)
types = {0: ' ', 1: '#'}
n_coords = [(0, -1), (1, 0), (0, 1), (-1, 0)] # coordinates of neighbours


################### Helper functions
def read_grid():
    g = dict()
    for r, l in enumerate(open('input.txt')):
        for c, x in enumerate(l.rstrip('\n')):
            if x == ' ':
                z = 0
            elif x in ['-', '+', '|']:
                z = 1
            g[(c, r)] = z
    grid_x, grid_y = max(x for x, _ in g.keys()) + 1, max(y for _, y in g.keys()) + 1
    return g, (grid_x, grid_y)

def print_grid(grid, dims):
    for r in range(dims[1]):
        print(''.join([types[grid[(c, r)]] for c in range(dims[0])]))


def print_path(grid, dims, path, start):
    for r in range(dims[1]):
        line = ''
        for c in range(dims[0]):
            if (c, r) == start:
                x = 'S'
            elif (c, r) in path:
                x = 'o'
            else:
                x = types[grid[(c, r)]]
            line += x
        print(line)

#################### the DFS algorithm ################

def DFS(grid, dims, start):
    #visited = set()
    path = [start]
    stack = deque([(start, path)])

    while stack:
        v, path = stack.pop()

        #if v not in visited:
        #    visited.add(v)

            # find all neighbours of v
        for n in n_coords:
            v_next = (v[0] + n[0], v[1] + n[1])
            if (v_next in grid 
                and v_next not in path 
                and grid[v_next] != 1):
                stack.append((v_next, path + [v]))
        
            # if neighbour not in visited, put it onto the stack and append v to the path

    return path
