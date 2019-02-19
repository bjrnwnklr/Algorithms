import bw_grid
from collections import deque

g = bw_grid.BW_Grid(50, 50, 60)

g.print_grid()

s = g.rand_select()

print(s)

##### flood fill example
q = deque([s])
seen = []
fill = 'x'

while q:
    v = q.pop()

    if v not in seen:
        seen.append(v)

        for n in g.neighbours(v):
            if n not in seen:
                q.appendleft(n)

g.print_path(seen, s, (-1, -1))


