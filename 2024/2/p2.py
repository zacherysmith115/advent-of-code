#! /usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.readlines()
    reports = [tuple(int(s) for s in line.split(" ")) for line in lines]


def safe(report: list[int]) -> bool:
    deltas = [x2 - x1 for x2, x1 in zip(report[1:], report[:-1])]

    all_increasing_or_decreasing = all([d > 0 for d in deltas]) or all(d < 0 for d in deltas)

    return all_increasing_or_decreasing and all(abs(d) < 4 for d in deltas)


nsafe = 0
for report in reports:
    nlevels = len(report)

    if safe(report):
        nsafe += 1
    else:
        matrix = [[level for level in report] for _ in range(nlevels)]
        matrix = [[matrix[i][j] for j in range(nlevels) if i != j] for i in range(nlevels)]

        for report in matrix:
            if safe(report):
                nsafe += 1
                break

print(nsafe)
