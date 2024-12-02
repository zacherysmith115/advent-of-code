#! /usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [tuple(s for s in line.split() if s) for line in lines]

xs = [int(x) for x, _ in lines]
ys = [int(y) for _, y in lines]

xs.sort()
ys.sort()

summed_differences = sum(abs(x - y) for x, y in zip(xs, ys))

print(summed_differences)