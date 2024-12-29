#! /usr/bin/env python3

from __future__ import annotations
from typing import NewType

point = NewType("point", tuple[int, int])
grid = NewType("grid", list[list[str]])


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]


class Region:
    N: int

    def __init__(self, plant: str, region: set[point]):
        self.plant = plant
        self.region = region
        self.corners = []

    def __eq__(self, value: Region) -> bool:
        return self.region == value.region and self.plant == value.plant

    def area(self) -> int:
        return len(self.region)

    def nsides(self, g: grid) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        caddy = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        corners = [(d1, c, d2) for d1, d2, c in zip(directions, directions[1:] + directions[:1], caddy)]

        nsides = 0
        for i, j in self.region:
            for corner in corners:
                adjacents = [(i + di, j + dj) for di, dj in corner]

                # Outside corner
                if all(adjacent not in self.region for adjacent in adjacents):
                    self.corners.append((i, j))
                    nsides += 1

                # Insider corner
                if [1 if adjacent in self.region else 0 for adjacent in adjacents] == [1, 0, 1]:
                    self.corners.append((i, j))
                    nsides += 1

                # Adjacent corners
                if [1 if adjacent in self.region else 0 for adjacent in adjacents] == [0, 1, 0]:
                    self.corners.append((i, j))
                    nsides += 1

        return nsides

    @staticmethod
    def bounded(i: int, j: int) -> bool:
        return 0 <= i < Region.N and 0 <= j < Region.N

    def _border(self) -> list[point]:
        return sorted(
            [
                (i, j)
                for i, j in self.region
                if not all(
                    [
                        (i - 1, j) in self.region,
                        (i, j + 1) in self.region,
                        (i + 1, j) in self.region,
                        (i, j - 1) in self.region,
                    ]
                )
            ]
        )

    def __eq__(self, region2: Region) -> bool:
        return all(r in self.region for r in region2.region)

    def __repr__(self):
        m = [["." if (i, j) not in self.region else self.plant for j in range(Region.N)] for i in range(Region.N)]
        for i, j in self.corners:
            m[i][j] = "*"
        return "\n".join([" ".join(row) for row in m]) + "\n"

    @staticmethod
    def bfs(g: grid, start: point) -> Region:

        if not Region.bounded(*start):
            raise ValueError(f"Unbonded index {start}")

        region = set()

        def _bfs(i: int, j: int) -> None:

            if (i, j) in region:
                return

            region.add((i, j))

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            moves = [(i + di, j + dj) for di, dj in directions]

            for i2, j2 in moves:
                if not Region.bounded(i2, j2):
                    continue

                if g[i2][j2] == g[i][j]:
                    _bfs(i2, j2)

        _bfs(*start)

        i, j = start
        return Region(g[i][j], region)


g = [[plant for plant in line] for line in lines]
Region.N = len(g)


regions: list[Region] = []
indices = [(i, j) for i in range(Region.N) for j in range(Region.N)]

for index in indices:
    region = Region.bfs(g, index)

    if region not in regions:
        regions.append(region)

prices = [region.area() * region.nsides(g) for region in regions]
print(sum(prices))
