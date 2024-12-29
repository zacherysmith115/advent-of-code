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


def rules(stone: int) -> tuple[int, ...]:
    if stone == 0:
        return (1,)
    elif ndigits(stone) % 2 == 0:
        return split(stone)
    else:
        return (stone * 2024,)


stones = [int(s) for s in line.split(" ")]

cache = {}
stone_counts = {stone: 1 for stone in stones}


BLINKS = 75
for _ in range(BLINKS):
    stones = [(stone, count) for stone, count in stone_counts.items() if count]
    for stone, count in stones:

        if stone not in cache:
            cache[stone] = rules(stone)

        for newstone in cache[stone]:
            if newstone not in stone_counts:
                stone_counts[newstone] = 0

            stone_counts[newstone] += count

        stone_counts[stone] -= count

print(sum(count for count in stone_counts.values()))
