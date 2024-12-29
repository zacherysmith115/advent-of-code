#! /usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

WIDTH = 101
HEIGHT = 103


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int

    @staticmethod
    def from_str(s: str) -> Robot:
        position, velocity = s.split(" ")
        x, y = [int(c) for c in position.removeprefix("p=").split(",")]
        dx, dy = [int(c) for c in velocity.removeprefix("v=").split(",")]

        return Robot(x, y, dx, dy)

    def move(self):
        self.x = (self.x + self.dx) % WIDTH
        self.y = (self.y + self.dy) % HEIGHT


robots = [Robot.from_str(line) for line in lines]

for _ in range(100):
    for robot in robots:
        robot.move()

m = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
for robot in robots:
    m[robot.y][robot.x] += 1

quadrants = [
    [[e for e in row[: WIDTH // 2]] for row in m[: HEIGHT // 2]],
    [[e for e in row[WIDTH // 2 + 1 :]] for row in m[: HEIGHT // 2]],
    [[e for e in row[: WIDTH // 2]] for row in m[HEIGHT // 2 + 1 :]],
    [[e for e in row[WIDTH // 2 + 1 :]] for row in m[HEIGHT // 2 + 1 :]],
]

n1, n2, n3, n4 = [sum(e for row in q for e in row) for q in quadrants]
safety_factor = n1 * n2 * n3 * n4

print(safety_factor)
