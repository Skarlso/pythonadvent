from functools import reduce

grid = [[False for i in range(1000)] for j in range(1000)]

with open('input.txt') as f:
    for line in f:
        line.rstrip()
        split = line.split()
        if split[0] == "turn":
            fromx, fromy = map(int, split[2].split(","))
            tox, toy = map(int, split[4].split(","))
            for i in range(fromx, tox):
                for j in range(fromy, toy):
                    if split[1] == "on":
                        grid[i][j] = True
                    elif split[1] == "off":
                        grid[i][j] = False
        elif split[0] == "toggle":
            fromx, fromy = map(int, split[1].split(","))
            tox, toy = map(int, split[3].split(","))
            for i in range(fromx, tox):
                for j in range(fromy, toy):
                    grid[i][j] = not grid[i][j]

turnedOn = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j]:
            turnedOn += 1

print(turnedOn)
