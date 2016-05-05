
total = 0
with open("input.txt") as f:
    for line in f:
        line.rstrip()
        split = list(map(lambda x: int(x), line.split("x")))
        l = split[0]
        w = split[1]
        h = split[2]
        total += (2 * l * w) + (2 * w * h) + (2 * h * l)
        split.sort()
        total += split[0] * split[1]

print(total)
