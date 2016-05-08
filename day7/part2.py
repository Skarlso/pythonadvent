from functools import reduce

grid = [[0 for i in range(1000)] for j in range(1000)]

with open('input.txt') as f:
    data = f.readlines()

for line in data:
    line.rstrip()
    split = line.split()
    fromx, fromy, tox, toy = 0, 0, 0, 0
    if split[0] == "turn":
        fromx, fromy = map(int, split[2].split(","))
        tox, toy = map(int, split[4].split(","))
    elif split[0] == "toggle":
        fromx, fromy = map(int, split[1].split(","))
        tox, toy = map(int, split[3].split(","))

    for i in range(fromx, tox + 1):
        for j in range(fromy, toy + 1):
            if split[0] == "turn":
                if split[1] == "on":
                    grid[i][j] += 1
                else:
                    grid[i][j] -= 1
            elif split[0] == "toggle":
                grid[i][j] += 2

turnedOn = 0
for i in range(1000):
    for j in range(1000):
        turnedOn += grid[i][j]

print(turnedOn)
