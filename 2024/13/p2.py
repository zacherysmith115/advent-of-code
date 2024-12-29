#! /usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass

with open("input.txt", "r") as f:
    lines = f.read()


@dataclass
class Button:
    x: int
    y: int

    @staticmethod
    def from_str(s: str) -> Button:
        _, _, x, y = s.split(" ")

        return Button(
            x=int(x.strip("X+")),
            y=int(y.strip("Y+")),
        )


@dataclass
class Prize:
    x: int
    y: int

    @staticmethod
    def from_str(s: str) -> Prize:
        _, x, y = s.split(" ")

        return Prize(
            x=int(x.strip("X=")) + 10000000000000,
            y=int(y.strip("Y=")) + 10000000000000,
        )


class Game:
    def __init__(self, a: Button, b: Button, prize: Prize) -> Game:
        self.a = a
        self.b = b
        self.prize = prize

    def play(self) -> int:
        """
        Satisfy these two equations:

        self.a.x * a + self.b.x * b = self.prize.x
        self.a.y * a + self.b.y * b = self.prize.y

        a1 * x + b1 * y = c1
        a2 * x + b2 * y = c2

        x = (b2 * c1 - b1 * c2) / (a1 * b2  - a2 * b1)
        y = (a1 * c2 - a2 * c1) / (a1 * b2  - a2 * b1)

        """
        a = (self.b.y * self.prize.x - self.b.x * self.prize.y) / (self.a.x * self.b.y - self.a.y * self.b.x)
        b = (self.a.x * self.prize.y - self.a.y * self.prize.x) / (self.a.x * self.b.y - self.a.y * self.b.x)

        cost = a * 3 + b

        return int(cost) if cost % 1 == 0 else 0

    @staticmethod
    def from_str(s: str) -> Game:
        a, b, prize = s.replace(",", "").split("\n")

        return Game(
            a=Button.from_str(a),
            b=Button.from_str(b),
            prize=Prize.from_str(prize),
        )

    def __repr__(self):
        return "\n".join(
            [
                f"Button A: X+{self.a.x}, Y+{self.a.y}",
                f"Button A: X+{self.b.x}, Y+{self.b.y}",
                f"Prize: X={self.prize.x}, Y={self.prize.y}",
                "",
            ]
        )


games = [Game.from_str(g) for g in lines.split("\n\n")]

costs = [game.play() for game in games]

print(sum(costs))
