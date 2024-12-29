#! /usr/bin/env python3


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

top = [[int(c) for c in line] for line in lines]
n = len(top)

trailheads = [(i, j) for i in range(n) for j in range(n) if top[i][j] == 0]


def traverse(top: list[list[int]], i: int, j: int):
    n = len(top)

    if top[i][j] == 9:
        return 1

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    move = []
    for di, dj in directions:
        i2, j2 = (i + di, j + dj)

        if i2 < 0 or i2 >= n or j2 < 0 or j2 >= n:
            continue

        if top[i2][j2] != top[i][j] + 1:
            continue

        move.append((i2, j2))

    return sum(traverse(top, i2, j2) for i2, j2 in move)


ratings = []
for i, j in trailheads:
    rating = traverse(top, i, j)
    ratings.append(rating)

print(sum(ratings))
