from collections import defaultdict
from heapq import heappush, heappop
import random

# generate a simple grid with each node in the grid having one of 
# two terrain types (0 - accessible, 1 - wall, inaccessible). Each step costs 1, 
# walls are inaccessible.
GRID_SIZE = 10
TYPES = 2
PERC_GROUND = 75 # how many % of the grid is covered by normal ground (rest is walls)
types = {0: '.', 1: '#'}
n_coords = [(0, -1), (1, 0), (0, 1), (-1, 0)] # coordinates of neighbours


################### Helper functions

def gen_grid():
    grid = {(c, r): 1 if c == 0 or r == 0 or c == GRID_SIZE - 1 or r == GRID_SIZE - 1 else 0 
            for c in range(GRID_SIZE) for r in range(GRID_SIZE)}
    for r in range(1, GRID_SIZE - 1):
        for c in range(1, GRID_SIZE - 1):
            grid[(c, r)] = random.choices([0, 1], cum_weights = [PERC_GROUND, 100])[0]
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

# randomly select coordinates within the grid and return them if they are not walls
# can be used to generate random start and target coordinates
def rand_select(grid):
    while True:
        c, r = random.randrange(1, GRID_SIZE - 1), random.randrange(1, GRID_SIZE - 1)
        if grid[(c, r)] == 0: return (c, r)


############ run an example
def run_example():
    grid = gen_grid()
    # pick start and target coordinates
    start = rand_select(grid)
    target = rand_select(grid)
    came_from, cost_so_far = a_star(grid, start, target)
    
    # check if we found a path
    if came_from[target]:
        p = reconstruct_path(came_from, start, target)
        print_path(grid, p, start, target)
        print('From %s to %s: %d steps' % (str(start), str(target), cost_so_far[target]))
    else:
        print('No path from %s to %s found.' % (str(start), str(target)))

############## A* algorithm
# uses Manhattan heuristic to determine heuristic distance
def heuristic(a, b):
    (c1, r1) = a
    (c2, r2) = b
    return abs(c1 - c2) + abs(r1 - r2)

def reconstruct_path(came_from, start, target):
    current = target
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path


# returns a dictionary of paths from start to each accessible square in the grid
def a_star(grid, start, target):
    frontier = [(0, start)]     # our priority queue with starting values
    came_from = defaultdict(list)   # path of visited nodes
    cost_so_far = {start: 0}    # cost of the path so far

    while frontier:
        _, current = heappop(frontier)

        if current == target:
            break

        for n in n_coords:
            v_next = (current[0] + n[0], current[1] + n[1])
            # check if neighbour is a valid grid component
            if (v_next in grid 
                and grid[v_next] != 1):
                new_cost = cost_so_far[current] + 1 # cost for moving in grid is always 1 - change if there is a specific cost for movements e.g. for terrain
                # if we have not found cost for v_next, or found
                # a cheaper path to v_next, add it to the queue
                if (v_next not in cost_so_far or 
                    new_cost < cost_so_far[v_next]):
                    cost_so_far[v_next] = new_cost
                    # estimate the cost to the goal
                    priority = new_cost + heuristic(target, v_next)
                    heappush(frontier, (priority, v_next))
                    came_from[v_next] = current
                
    return came_from, cost_so_far