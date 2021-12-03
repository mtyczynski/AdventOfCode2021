from aoc import read_input
from collections import defaultdict

data = read_input(3)
datalen = max(map(len, data))
oxygen = co2 = data

defdict = defaultdict(lambda: defaultdict(int))
for seq in data:
    for i, char in enumerate(seq):
        defdict[char][i] += 1

max = min = ""
for i in range(datalen):
    max += '1' if defdict['1'][i] > defdict['0'][i] else '0'
    min += '0' if defdict['1'][i] > defdict['0'][i] else '1'

###### PART 2 ######
sequence = ""
for k in range(datalen):
    nums = {"0":0, "1":0}
    for seq in oxygen:
        nums[seq[k]] += 1
    sequence += "1" if nums["1"] >= nums["0"] else "0"
    oxygen = list(filter(lambda x: x.startswith(sequence), oxygen))

sequence = ""
for k in range(datalen):
    nums = {"0":0, "1":0}
    for seq in co2:
        nums[seq[k]] += 1
    sequence += "0" if nums["0"] <= nums["1"] else "1"
    co2 = list(filter(lambda x: x.startswith(sequence), co2))
    if len(co2) == 1: break


###### RESULTS #######
max_int = int(max, 2)
min_int = int(min, 2)
print(f"part1 result: {max_int*min_int}")

oxygen_int = int(oxygen[0], 2)
co2_int = int(co2[0], 2)
print(f"part2 result: {oxygen_int * co2_int}")