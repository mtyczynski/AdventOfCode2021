from aoc import *

data = read_input(7, int, ",")

min_fuel = float("inf")
min_fuel2 = float("inf")


for crab_position in range(min(data), max(data)):
    fuel1 = 0
    fuel2 = 0
    for crab in data:
        distance = abs(crab_position-crab)
        fuel1 += distance
        fuel2 += distance*(distance+1)/2
    min_fuel = min(min_fuel, fuel1)
    min_fuel2 = min(min_fuel2, fuel2)

print(f"part1: {min_fuel}, part2: {min_fuel2}")