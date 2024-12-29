#! /usr/bin/env python3


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]
    lines = [(s.strip() for s in line.split(":")) for line in lines]


equations = [(int(testvalue), [int(op) for op in operators.split(" ")]) for testvalue, operators in lines]


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def isvalid(expected: int, calculated: int, operators: list[int]):
    if not operators:
        return expected == calculated

    op, *operators = operators

    return (
        isvalid(expected, calculated + op, operators)
        or isvalid(expected, calculated * op, operators)
        or isvalid(expected, concat(calculated, op), operators)
    )


total = 0
for testvalue, operators in equations:
    op1, op2, *operators = operators

    if (
        isvalid(testvalue, op1 + op2, operators)
        or isvalid(testvalue, op1 * op2, operators)
        or isvalid(testvalue, concat(op1, op2), operators)
    ):
        total += testvalue

print(total)
