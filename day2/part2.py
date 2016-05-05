from functools import reduce

total = 0
with open("input.txt") as f:
    for line in f:
        line.rstrip()
        split = list(map(lambda x: int(x), line.split("x")))
        split.sort()
        total += (2 * split[0]) + (2 * split[1])
        # this might be overdoing it... But I like it.
        total += reduce(lambda x, y: x * y, split)

print(total)
