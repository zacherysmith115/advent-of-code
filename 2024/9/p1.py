#! /usr/bin/env python3


with open("input.txt", "r") as f:
    line, *_ = [line.strip() for line in f]


disk = []
for i, c in enumerate(line):
    size = int(c)
    value = -1 if i % 2 else i // 2

    disk.extend([value] * size)

lptr = 0
rptr = len(disk) - 1

while lptr < rptr:
    while disk[lptr] != -1:
        lptr += 1

    while disk[rptr] == -1:
        rptr -= 1

    disk[lptr], disk[rptr] = disk[rptr], disk[lptr]

disk[lptr], disk[rptr] = disk[rptr], disk[lptr]

pivot = disk.index(-1)
disk = disk[:pivot]

xsum = sum([i * id for i, id in enumerate(disk) if id])
print(xsum)
