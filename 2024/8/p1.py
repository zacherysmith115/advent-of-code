#! /usr/bin/env python3


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

keys = {c for line in lines for c in line if c != "."}
grid = [[c for c in line] for line in lines]

n = len(grid)

antennas: dict[str, list[tuple[int, int]]]
antennas = {key: [] for key in keys}

for i in range(n):
    for j in range(n):

        antenna = grid[i][j]
        if antenna != ".":
            location = (i, j)
            antennas[antenna].append(location)

antinodes = [[0 for _ in range(n)] for _ in range(n)]

for locations in antennas.values():

    for i1, j1 in locations:
        for i2, j2 in locations:
            if i1 == i2 and j1 == j2:
                continue

            j3 = (j2 - j1) * -1 + j1
            i3 = (i2 - i1) * -1 + i1

            if i3 < 0 or i3 >= n or j3 < 0 or j3 >= n:
                continue

            antinodes[i3][j3] += 1


print(sum(1 for i in range(n) for j in range(n) if antinodes[i][j]))
