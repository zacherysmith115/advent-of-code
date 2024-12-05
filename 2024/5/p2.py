#! /usr/bin/env python3

with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

pivot = lines.index("")

edges = [tuple(int(x) for x in line.split("|")) for line in lines[:pivot]]
paths = [[int(c) for c in line.split(",")] for line in lines[pivot + 1 :]]


n = max(e for edge in edges for e in edge) + 1
graph = [[0 for _ in range(n)] for _ in range(n)]

for i, j in edges:
    graph[i][j] = 1

invalid: list[list[int]] = []
for path in paths:
    if not all(graph[i][j] for i, j in zip(path, path[1:])):
        invalid.append(path)

corrected: list[list[int]] = []

for path in invalid:
    fixed = []
    remaining = path.copy()

    i = remaining.pop(0)
    fixed.append(i)

    while remaining:
        j = remaining.pop(0)

        if graph[fixed[-1]][j]:
            fixed.append(j)
        elif graph[j][fixed[0]]:
            fixed.insert(0, j)
        else:
            for a, b in zip(fixed, fixed[1:]):
                if graph[a][j] and graph[j][b]:
                    fixed.insert(fixed.index(a) + 1, j)
                    break
            else:
                remaining.append(j)

    corrected.append(fixed)

print(sum(p[len(p) // 2] for p in corrected))
