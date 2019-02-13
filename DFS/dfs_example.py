from collections import deque

# generate a simple grid with each node in the grid having one of 
# two terrain types (0 - accessible, 1 - wall, inaccessible). Each step costs 1, 
# walls are inaccessible.
#
# maze generated from http://www.delorie.com/game-room/mazes/genmaze.cgi


TYPES = 2
start = (0, 1)
types = {0: ' ', 1: '#'}
n_coords = [(0, -1), (1, 0), (0, 1), (-1, 0)] # coordinates of neighbours


################### Helper functions
def read_grid():
    g = dict()
    for r, l in enumerate(open(r'input.txt')):
        for c, x in enumerate(l.rstrip('\n')):
            if x == ' ':
                z = 0
            elif x in ['-', '+', '|']:
                z = 1
            g[(c, r)] = z
    grid_x, grid_y = max(x for x, _ in g.keys()) + 1, max(y for _, y in g.keys()) + 1
    target = (grid_x - 1, grid_y - 2)
    return g, (grid_x, grid_y), target

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

#### main program ####
g, dims, target = read_grid()
p = DFS(g, dims, start, target)