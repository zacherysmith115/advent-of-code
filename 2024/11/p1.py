#! /usr/bin/env python3


with open("input.txt", "r") as f:
    line, *_ = [line.strip() for line in f]


def ndigits(x: int) -> int:
    cnt = 0

    while x > 0:
        x //= 10
        cnt += 1

    return cnt


def split(x: int) -> tuple[int, int]:
    n = ndigits(x)
    divisor = 10 ** (n // 2)
    return x // divisor, x % divisor


stones = [int(s) for s in line.split(" ")]

n = 25
for _ in range(n):
    new = []

    for stone in stones:
        if stone == 0:
            new.append(1)
        elif ndigits(stone) % 2 == 0:
            new.extend(split(stone))
        else:
            new.append(stone * 2024)

    stones = new

# TODO: not right :[
print(len(stones))
