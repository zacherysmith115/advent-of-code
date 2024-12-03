#! /usr/bin/env python3

import re

with open("input.txt", "r") as f:
    lines = f.readlines()
    instructions = "".join(lines)

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, instructions)

print(sum(int(x) * int(y) for x, y in matches))
