#! /usr/bin/env python3

from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def move(self, position: tuple[int, int]) -> tuple[int, int]:
        return (pos + delta for pos, delta in zip(position, self.value))


def isloop(
    m: list[list[int]], position: tuple[int, int], directions: list[Direction]
) -> tuple[bool, tuple[int, int] | None]:

    m = [row.copy() for row in m]
    directions = directions.copy()

    n = len(m)
    i, j = position
    m[i][j] = "X"

    direction = directions.pop(0)

    # Make the first two sides of the loop
    while len(directions) > 1:
        i, j = direction.move(position)

        if i < 0 or i >= n or j < 0 or j >= n:
            return False, None

        if m[i][j] == "#":
            direction = directions.pop(0)
            continue

        m[i][j] = "X"
        position = (i, j)

    # Search for a place to close the loop
    while True:
        i, j = direction.move(position)

        if i < 0 or i >= n or j < 0 or j >= n:
            return False, None

        match directions[0]:
            case Direction.UP:
                values = [m[k][j] for k in range(0, i)]
                values.reverse()
            case Direction.DOWN:
                values = [m[k][j] for k in range(i + 1, n)]
            case Direction.RIGHT:
                values = [m[i][k] for k in range(j + 1, n)]
            case Direction.LEFT:
                values = [m[i][k] for k in range(0, j)]
                values.reverse()
            case _:
                raise ValueError(f"Unexpected direction: {directions[0]}")

        if m[i][j] == "#":
            return False, None

        m[i][j] = "X"
        position = (i, j)

        if any((a == "X" and b == "X") or (a == "X" and b == "#") for a, b in zip(values, values[1:])):
            break

    m[i][j] = "X"
    obj_i, obj_j = direction.move(position)

    if m[obj_i][obj_j] == "^":
        return False, None

    m[obj_i][obj_j] = "O"

    # Verify the path exists
    direction = directions.pop(0)
    while True:
        i, j = direction.move(position)

        if m[i][j] == "#":
            return False, None

        if m[i][j] == "X":
            return True, (obj_i, obj_j)

        m[i][j] = "X"
        position = (i, j)


with open("example.txt", "r") as f:
    lines = [line.rstrip() for line in f]

matrix = [[c for c in line] for line in lines]
n = len(matrix)


for i in range(n):
    for j in range(n):
        if matrix[i][j] == "^":
            position = (i, j)

q = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
direction = q.pop(0)

object_locations = []
while True:
    i, j = direction.move(position)

    if i < 0 or i >= n or j < 0 or j >= n:
        break

    if matrix[i][j] == "#":
        q.append(direction)

        exist, location = isloop(matrix, position, q)

        if exist and location not in object_locations:
                object_locations.append(location)

        direction = q.pop(0)
        continue

    matrix[i][j] = "X"
    position = (i, j)


# TODO: not right :[
print(object_locations)
n = len(object_locations)
assert n != 83
print(n)
