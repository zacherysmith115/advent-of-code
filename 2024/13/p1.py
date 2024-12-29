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
            x=int(x.strip("X=")),
            y=int(y.strip("Y=")),
        )


class Game:
    def __init__(self, a: Button, b: Button, prize: Prize) -> Game:
        self.a = a
        self.b = b
        self.prize = prize

    def play(self) -> int:
        costs = []

        for i in range(100):
            for j in range(100):
                onx = i * self.a.x + j * self.b.x == self.prize.x
                ony = i * self.a.y + j * self.b.y == self.prize.y

                if onx and ony:
                    costs.append(i * 3 + j)

        return min(costs) if costs else 0

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

print(sum(game.play() for game in games))
