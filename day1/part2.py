from functools import reduce

with open('input.txt', 'r') as f:
    data = f.read().replace('\n', '')

location = 1
index = 0

for i, ch in enumerate(data):
    if ch == '(':
        location += 1
    else:
        location -= 1

    if location < 0:
        index = i
        break

print(index)
