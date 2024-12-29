#! /usr/bin/env python3
from __future__ import annotations

with open("input.txt", "r") as f:
    m, moves = f.read().split("\n\n")

m = [[c for c in line.strip()] for line in m.split("\n")]
moves = moves.replace("\n", "")

assert len(m) == len(m[0])
N = len(m)

for i in range(N):
    for j in range(N):
        if m[i][j] == "@":
            break
    else:
        continue

    break


for move in moves:
    match move:
        case "^":
            if m[i - 1][j] == "#":
                continue
            elif m[i - 1][j] == ".":
                pass
            elif m[i - 1][j] == "O":

                for k in range(i - 1, 0, -1):
                    if m[k][j] == ".":
                        break

                    if m[k][j] == "#":
                        break
                else:
                    continue

                if m[k][j] == "#":
                    continue

                for k in range(k, i - 1):
                    m[k + 1][j], m[k][j] = m[k][j], m[k + 1][j]

            m[i - 1][j], m[i][j] = m[i][j], m[i - 1][j]
            i -= 1

        case ">":
            if m[i][j + 1] == "#":
                continue
            elif m[i][j + 1] == ".":
                pass
            elif m[i][j + 1] == "O":

                for k in range(j + 1, N):
                    if m[i][k] == ".":
                        break

                    if m[i][k] == "#":
                        break
                else:
                    continue

                if m[i][k] == "#":
                    continue

                for k in range(k, j + 1, -1):
                    m[i][k - 1], m[i][k] = m[i][k], m[i][k - 1]

            m[i][j + 1], m[i][j] = m[i][j], m[i][j + 1]
            j += 1

        case "v":
            if m[i + 1][j] == "#":
                continue
            elif m[i + 1][j] == ".":
                pass
            elif m[i + 1][j] == "O":

                for k in range(i + 1, N):
                    if m[k][j] == ".":
                        break

                    if m[k][j] == "#":
                        break
                else:
                    continue

                if m[k][j] == "#":
                    continue

                for k in range(k, i + 1, -1):
                    m[k - 1][j], m[k][j] = m[k][j], m[k - 1][j]

            m[i + 1][j], m[i][j] = m[i][j], m[i + 1][j]
            i += 1

        case "<":
            if m[i][j - 1] == "#":
                continue
            elif m[i][j - 1] == ".":
                pass
            elif m[i][j - 1] == "O":

                for k in range(j - 1, 0, -1):
                    if m[i][k] == ".":
                        break

                    if m[i][k] == "#":
                        break
                else:
                    continue

                if m[i][k] == "#":
                    continue

                for k in range(k, j - 1):
                    m[i][k + 1], m[i][k] = m[i][k], m[i][k + 1]

            m[i][j - 1], m[i][j] = m[i][j], m[i][j - 1]
            j -= 1

        case _:
            raise ValueError(move)

tiles = [(i, j) for i in range(N) for j in range(N)]
coordinates = [(i, j) for i, j in tiles if m[i][j] == "O"]
print(sum(100 * i + j for i, j in coordinates))
