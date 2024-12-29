#! /usr/bin/env python3

from __future__ import annotations
from typing import NewType

point = NewType("point", tuple[int, int])
matrix = NewType("matrix", list[list[int]])


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]


class Region:
    def __init__(self, plant: str, region: list[point], n: int):
        self.plant = plant
        self.region = region
        self.n = n

    def perimeter(self) -> int:
        border = self._border()

        cnt = 0

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i, j in border:
            cnt += sum(1 for di, dj in directions if (i + di, j + dj) not in self.region)

        return cnt

    def area(self) -> int:
        return len(self.region)

    def _border(self) -> list[point]:
        return [
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

    def subregion(self, regions: list[Region]) -> tuple[bool, Region | None]:
        border = self._border()

        for region in regions:
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            shared = [(i + di, j + dj) for di, dj in directions for i, j in border]

            if all((point in self.region or point in region.region) for point in shared):
                return True, region

        return False, None

    def __eq__(self, region2: Region) -> bool:
        return all(r in self.region for r in region2.region)

    def __repr__(self):
        m = [["." if (i, j) not in self.region else self.plant for j in range(self.n)] for i in range(self.n)]
        return "\n".join([" ".join(row) for row in m]) + "\n"

    @staticmethod
    def traverse(m: matrix, i: int, j: int) -> Region:

        n = len(m)
        if not (0 <= i < n and 0 <= j < n):
            raise ValueError(f"Unbonded index ({i}, {j})")

        region: list[point] = []

        def _traverse(i: int, j: int) -> None:
            if (i, j) in region:
                return

            region.append((i, j))

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for i2, j2 in [(i + di, j + dj) for di, dj in directions]:
                if not (0 <= i2 < n and 0 <= j2 < n):
                    continue

                if m[i2][j2] == m[i][j]:
                    _traverse(i2, j2)

        _traverse(i, j)

        return Region(m[i][j], region, n)


m = [[c for c in line] for line in lines]
n = len(m)

regions: list[Region] = []
for i in range(n):
    for j in range(n):
        region = Region.traverse(m, i, j)

        if region not in regions:
            regions.append(region)


prices = [region.area() * region.perimeter() for region in regions]
print(sum(prices))
