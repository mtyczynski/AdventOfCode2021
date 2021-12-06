from aoc import *
from collections import defaultdict

cross1 = defaultdict(int)
cross2 = defaultdict(int)

crossings = lambda x: sum(val > 1 for val in x.values())
dist = lambda x, y: (abs(y-x), sign(y-x))

data = map(integers, read_input(5))

for x1, y1, x2, y2 in data:
    dist_x, sign_x = dist(x1, x2)
    dist_y, sign_y = dist(y1, y2)
    for i in range(max(dist_x, dist_y)+1):
        x = x1 + i*sign_x
        y = y1 + i*sign_y
        if dist_x == 0 or dist_y == 0:
            cross1[(x, y)] += 1
        cross2[(x, y)] += 1

print(f"part1: {crossings(cross1)}, part2: {crossings(cross2)}")
