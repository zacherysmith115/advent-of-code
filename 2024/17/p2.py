#! /usr/bin/env python3

from __future__ import annotations


class Computer:
    def __init__(self, a: int, b: int, c: int, program: list[int]) -> Computer:
        self.a = a
        self.b = b
        self.c = c

        self._ptr = 0
        self.program = program
        self.output = []

    def _combo(self, operand: int) -> int:
        if 0 <= operand <= 3:
            return operand

        elif operand == 4:
            return self.a

        elif operand == 5:
            return self.b

        elif operand == 6:
            return self.c

        else:
            raise ValueError(operand)

    def _adv(self, operand: int) -> None:
        self.a = self.a // (2 ** self._combo(operand))
        self._ptr += 2

    def _bxl(self, operand: int):
        self.b = self.b ^ operand
        self._ptr += 2

    def _bst(self, operand: int) -> None:
        self.b = self._combo(operand) % 8
        self._ptr += 2

    def _jnz(self, operand: int) -> None:
        if self.a == 0:
            self._ptr += 2
            return

        self._ptr = operand

    def _bxc(self, _: int) -> None:
        self.b = self.b ^ self.c
        self._ptr += 2

    def _out(self, operand: int) -> None:
        self.output.append(self._combo(operand) % 8)
        self._ptr += 2

    def _bdv(self, operand: int) -> None:
        self.b = self.a // (2 ** self._combo(operand))
        self._ptr += 2

    def _cdv(self, operand: int) -> None:
        self.c = self.a // (2 ** self._combo(operand))
        self._ptr += 2

    def compute(self) -> list[int]:
        while self._ptr < len(self.program):
            opcode, operand = self.program[self._ptr : self._ptr + 2]

            match opcode:
                case 0:
                    self._adv(operand)
                case 1:
                    self._bxl(operand)
                case 2:
                    self._bst(operand)
                case 3:
                    self._jnz(operand)
                case 4:
                    self._bxc(operand)
                case 5:
                    self._out(operand)
                case 6:
                    self._bdv(operand)
                case 7:
                    self._cdv(operand)
                case _:
                    raise ValueError(opcode)

        return self.output

    def __repr__(self) -> str:
        n = len("Program: ") + self._ptr * 2

        return "\n".join(
            [
                f"Register A: {self.a}",
                f"Register B: {self.b}",
                f"Register C: {self.c}",
                " " * n + "v",
                "Program: " + ",".join(str(p) for p in self.program),
                "",
                "Output: " + ",".join(str(x) for x in self.output),
                "",
            ]
        )


with open("input.txt", "r") as f:
    lines = [line.strip().split(": ") for line in f if line.strip()]

postfixes = [postfix for _, postfix in lines]
program = [int(p) for p in postfixes.pop().split(",")]
a, b, c = [int(x) for x in postfixes]


a = 0
while True:
    computer = Computer(a, b, c, program)
    output = computer.compute()
    if output == program:
        print(computer)
        break

    a += 1
print(a)

