# Cudos to reddit

import numpy as np
import re

lines = [l.strip() for l in open("input.txt", "r").readlines()]
grid = np.zeros((1000, 1000), dtype=int)

rx = re.compile(
    r"(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)")
for line in lines:
    op, x1, y1, x2, y2 = re.findall(rx, line)[0]

    x1 = int(x1)
    x2 = int(x2) + 1
    y1 = int(y1)
    y2 = int(y2) + 1

    if op == "turn on":
        grid[y1:y2, x1:x2] += 1

    if op == "turn off":
        grid[y1:y2, x1:x2] -= 1
        grid[grid < 0] = 0

    if op == "toggle":
        grid[y1:y2, x1:x2] += 2

print(np.sum(grid))
