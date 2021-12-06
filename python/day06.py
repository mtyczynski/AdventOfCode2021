from aoc import *
import numpy as np
data = np.array(mapl(integers, read_input(6))[0])
fishes_by_gen = np.array([0] * 9, dtype='int64')

for i in range(9):
    fishes_by_gen[i] = np.count_nonzero(data == i)

def birth(fishes):
    fishes = np.roll(fishes, -1)
    fishes[6]+=fishes[8]
    return fishes

def solve(fishes ,days):
    for i in range(days):
        fishes = birth(fishes)
    print(fishes.sum())

solve(fishes_by_gen, 80)
solve(fishes_by_gen, 256)