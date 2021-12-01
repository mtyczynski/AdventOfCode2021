from aoc import read_input


solve = lambda data, window: sum(a < b for a, b in zip(data, data[window:]))

data = read_input(1, int)
print(solve(data, 1))
print(solve(data, 3))
