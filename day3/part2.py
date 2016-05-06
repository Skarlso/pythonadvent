
with open("input.txt") as f:
    data = f.read().replace('\n', '')

dictionary = {}
x, y = 0, 0
rx, ry = 0, 0
counter = 0

for ch in data:
    robot = False if counter & 1 == 0 else True
    if ch == '^':
        if robot:
            y += 1
        else:
            ry += 1
    elif ch == '<':
        if robot:
            x -= 1
        else:
            rx -= 1
    elif ch == '>':
        if robot:
            x += 1
        else:
            rx += 1
    elif ch == 'v':
        if robot:
            y -= 1
        else:
            ry -= 1

    if robot:
        dictionary[(x, y)] = True
    else:
        dictionary[(rx, ry)] = True
    counter += 1

print(len(dictionary))
