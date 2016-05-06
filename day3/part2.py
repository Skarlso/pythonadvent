
with open("input.txt") as f:
    data = f.read().replace('\n', '')

dictionary = {}
x, y = 0, 0
rx, ry = 0, 0
counter = 0

for ch in data:
    robot = False if counter & 1 == 0 else True
    if robot:
        if ch == '^':
            y += 1
        elif ch == '<':
            x -= 1
        elif ch == '>':
            x += 1
        elif ch == 'v':
            y -= 1
        dictionary[(x, y)] = True
    else:
        if ch == '^':
            ry += 1
        elif ch == '<':
            rx -= 1
        elif ch == '>':
            rx += 1
        elif ch == 'v':
            ry -= 1
        dictionary[(rx, ry)] = True
    counter += 1

print(len(dictionary))
