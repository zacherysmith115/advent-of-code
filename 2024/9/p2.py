#! /usr/bin/env python3

from dataclasses import dataclass

with open("input.txt", "r") as f:
    line = f.read().strip()


@dataclass
class Memory:
    size: int
    fid: int

    def __str__(self):
        if self.fid == -1:
            return "." * self.size

        return str(self.fid) * self.size

    def __len__(self):
        return self.size


disk: list[Memory] = []
index, fid = 0, 0

for i, c in enumerate(line):
    size = int(c)

    if i % 2:
        disk.append(Memory(size, -1))

    else:
        disk.append(Memory(size, fid))
        fid += 1

rptr = len(disk) - 1

while rptr > 0:
    while disk[rptr].fid == -1:
        rptr -= 1

    lptr = 0
    while lptr < rptr:
        while disk[lptr].fid != -1 and lptr < rptr:
            lptr += 1

        space, file = disk[lptr], disk[rptr]
        if len(space) == len(file):
            disk[lptr], disk[rptr] = file, space
            break

        elif len(space) > len(file):
            rspace = Memory(len(file), -1)
            lspace = Memory(len(space) - len(file), -1)

            disk[lptr], disk[rptr] = file, rspace
            disk.insert(lptr + 1, lspace)
            break

        else:
            lptr += 1

    # print("".join(str(d) for d in disk))
    rptr -= 1

filesystem = []
for memory in disk:
    filesystem.extend([memory.fid] * memory.size)

xsum = sum(i * fid for i, fid in enumerate(filesystem) if fid != -1)
print(xsum)
