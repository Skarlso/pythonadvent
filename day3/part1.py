
with open("input.txt") as f:
    data = f.read().replace('\n', '')

dictionary = {}
x, y = 0, 0

for ch in data:
    if ch == '^':
        y += 1
    elif ch == '<':
        x -= 1
    elif ch == '>':
        x += 1
    elif ch == 'v':
        y -= 1

    dictionary[(x, y)] = True

print(len(dictionary))
