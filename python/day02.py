from aoc import read_input, mapl

def calc_distance(key, data):
    return sum([int(x[1]) for x in data if x[0] == key])

data = read_input(2)
data_clean = mapl(lambda s: s.split(), data)

ups = calc_distance('up', data_clean)
downs = calc_distance('down', data_clean)
forwards = calc_distance('forward', data_clean)

print ((downs-ups)*forwards)

aim = depth = 0
for key, value in data_clean:
    val = int(value)
    match key:
        case "up": aim -= val
        case "down": aim += val
        case "forward":
            depth += aim*val

print(depth * forwards)