import random

# generate a simple grid with each node in the grid having one of 
# two terrain types (0 - accessible, 1 - wall, inaccessible). Each step costs 1, 
# walls are inaccessible.

class BW_Grid():

    grid = dict()
    height = 40
    width = 40
    perc_ground = 75                # % of open ground
    types = {0: '.', 1: '#'}        # 2 types of ground: 0 = open floor, 1 = wall

    def __init__(self, height = 40, width = 40, perc_ground = 75):
        self.height, self.width = height, width
        self.perc_ground = perc_ground
        self.grid = {(c, r): 1 if c == 0 or r == 0 or c == width - 1 or r == height - 1 else 0 
            for c in range(width) for r in range(height)}
        for r in range(1, height - 1):
            for c in range(1, width - 1):
                self.grid[(c, r)] = random.choices([0, 1], cum_weights = [perc_ground, 100])[0]

        
    def read_grid(self):
        self.grid = dict()
        for r, l in enumerate(open('grid.txt')):
            for c, x in enumerate(l.rstrip()):
                self.grid[(c, r)] = int(x)
        return self.grid

        
    def write_grid(self):
        f = open('grid.txt', 'w')
        for r in range(self.height):
            f.write(''.join([str(self.grid[(c, r)]) for c in range(self.width)]) + '\n')
        f.close

        
    def print_grid(self):
        for r in range(self.height):
            print(''.join([self.types[self.grid[(c, r)]] for c in range(self.width)]))

    def print_path(self, path, start, target):
        for r in range(self.height):
            line = ''
            for c in range(self.width):
                if (c, r) == start:
                    x = 'S'
                elif (c, r) == target:
                    x = 'T'
                elif (c, r) in path:
                    x = 'o'
                else:
                    x = self.types[self.grid[(c, r)]]
                line += x
            print(line)

    # randomly select coordinates within the grid and return them if they are not walls
    # can be used to generate random start and target coordinates
    def rand_select(self):
        while True:
            c, r = random.randrange(1, self.width - 1), random.randrange(1, self.height - 1)
            if self.grid[(c, r)] == 0: return (c, r)



    def neighbours(self, v):
        n_coords = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        results = []
        for n in n_coords:
            v_next = (v[0] + n[0], v[1] + n[1])
            if v_next in self.grid and self.grid[v_next] != 1:
                results.append(v_next)
        return results



