#! /usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [tuple(s for s in line.split() if s) for line in lines]


xs = [int(x) for x, _ in lines]
ys = [int(y) for _, y in lines]

xs.sort()
ys.sort()

counts = [0 for _ in range(max(xs) + 1)]

for y in ys:
    if y in xs:
        counts[y] += 1

similiarity_scores = [x * counts[x] for x in xs]
print(sum(similiarity_scores))
