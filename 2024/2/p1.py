#! /usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.readlines()
    reports = [tuple(int(s) for s in line.split(" ")) for line in lines]

nsafe = 0
for report in reports:
    n = len(report)
    deltas = [x2 - x1 for x2, x1 in zip(report[1:], report[:-1])]

    if all([d > 0 for d in deltas]) or all(d < 0 for d in deltas):
        if all(abs(d) < 4 for d in deltas):
            nsafe += 1

print(nsafe)
