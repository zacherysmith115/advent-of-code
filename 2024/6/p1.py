#! /usr/bin/env python3


with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

matrix = [[c for c in line] for line in lines]
n = len(matrix)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "^":
            position = (i, j)
            matrix[i][j] = "X"

q = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = q.pop(0)
cnt = 1

while True:
    i, j = (pos + delta for pos, delta in zip(position, direction))

    if i < 0 or i >= n or j < 0 or j >= n:
        cnt += 1
        matrix[i][j] = "X"
        break

    if matrix[i][j] == "#":
        q.append(direction)
        direction = q.pop(0)
        continue

    position = (i, j)

    if matrix[i][j] != "X":
        cnt += 1
        matrix[i][j] = "X"

cnt = sum([1 for i in range(n) for j in range(n) if matrix[i][j] == "X"])
print(cnt)
