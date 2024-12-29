#! /usr/bin/env python3


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

top = [[int(c) for c in line] for line in lines]
n = len(top)

trailheads = [(i, j) for i in range(n) for j in range(n) if top[i][j] == 0]


def traverse(top: list[list[int]], i: int, j: int, endpoints: list[tuple[int, int]]):
    n = len(top)

    if top[i][j] == 9:
        endpoints.append((i, j))
        return

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for di, dj in directions:
        i2, j2 = (i + di, j + dj)

        if i2 < 0 or i2 >= n or j2 < 0 or j2 >= n:
            continue

        if top[i2][j2] != top[i][j] + 1:
            continue

        traverse(top, i2, j2, endpoints)


scores = []
for i, j in trailheads:
    endpoints = []
    traverse(top, i, j, endpoints)

    scores.append(len(set(endpoints)))

print(sum(scores))
