#! /usr/bin/env python3

import re


with open("input.txt", "r") as f:
    lines = f.readlines()
    instructions = "".join(lines)


mul = r"mul\((\d{1,3}),(\d{1,3})\)"
do = r"do\(\)"
dont = r"don't\(\)"
pattern = re.compile("|".join([mul, do, dont]))

enabled = True
operators = []
for match in re.finditer(pattern, instructions):
    substring = match.group()

    if not enabled:
        enabled = re.match(do, substring) is not None
        continue

    enabled = re.match(dont, substring) is None

    if enabled and re.match(mul, substring):
        operators.append(match.groups())

print(sum(int(x) * int(y) for x, y in operators))
