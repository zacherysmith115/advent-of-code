#! /usr/bin/env python3
from collections import deque

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

N = 70
NBYTES = 1024


byte_locations = [tuple(int(c) for c in line.split(",")) for line in lines]
byte_locations = [(y, x) for x, y in byte_locations]

grid = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i, j in byte_locations[:NBYTES]:
    grid[i][j] = 1


def bfs(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    queue = deque([(*start, 0)])

    visited = set()
    visited.add(start)

    while queue:
        i, j, dist = queue.popleft()

        if (i, j) == end:
            return dist

        for di, dj in directions:
            i2, j2 = i + di, j + dj

            if 0 <= i2 <= N and 0 <= j2 <= N and grid[i2][j2] == 0 and (i2, j2) not in visited:
                visited.add((i2, j2))
                queue.append((i2, j2, dist + 1))

    return -1


start = (0, 0)
end = (N, N)

result = bfs(grid, start, end)

print(result)
