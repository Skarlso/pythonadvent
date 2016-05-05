from functools import reduce

with open('input.txt', 'r') as f:
    data = f.read().replace('\n', '')

print(reduce(lambda x, y: x - 1 if y == ')' else x + 1, data, 0))
