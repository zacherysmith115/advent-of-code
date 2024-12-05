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

valid = []
for path in paths:
    if all(graph[i][j] for i, j in zip(path, path[1:])):
        valid.append(path)

print(sum(p[len(p) // 2] for p in valid))