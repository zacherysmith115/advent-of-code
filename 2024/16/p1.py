#! /usr/bin/env python3

from enum import Enum

class Direction(Enum):
    N = (-1, 0)
    E = (0, 1)
    S = (1, 0)
    W = (0, -1)


def traverse(maze: list[list[str]], path: list[tuple[int, int]], paths: list[list[tuple[int, int]]]) -> None:
    path = path.copy()

    i, j = path[-1]

    if maze[i][j] == "E":
        paths.append(path)
        return

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    moves = [(i + di, j + dj) for di, dj in directions]
    moves = [move for move in moves if move not in path]

    for i2, j2 in moves:
        if maze[i2][j2] == "." or maze[i2][j2] == "E":
            traverse(maze, path + [(i2, j2)], paths)


with open("example.txt", "r") as f:
    lines = [line.strip() for line in f]

maze = [[c for c in line] for line in lines]
N = len(maze)

for i in range(N):
    for j in range(N):
        if maze[i][j] == "S":
            break
    else:
        continue

    break


paths = []
path = [(i, j)]
traverse(maze, path, paths)


def cost(path: list[tuple[int, int]]) -> int:
    deltas = []
    for i in range(1, len(path)):
        i2, j2 = path[i]
        i1, j1 = path[i - 1]

        deltas.append(Direction((i2 - i1, j2 - j1)))

    nturns = sum(d2 is not d1 for d2, d1 in zip(deltas[1:], deltas))

    if deltas[0] is not Direction.E:
        nturns += 1

    return nturns * 1000 + len(deltas)


costs = [cost(path) for path in paths]
print(min(costs))
