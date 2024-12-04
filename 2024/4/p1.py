#! /usr/bin/env python3


with open("input.txt", "r") as f:
    crossword = [[char for char in line.strip()] for line in f]

N = len(crossword)
M = len(crossword[0])
XMAS = "XMAS"

directions = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]

count = 0
for i in range(N):
    for j in range(M):

        for direction in directions:
            buffer = ""

            for k in range(len(XMAS)):
                row = i + k * direction[0]
                col = j + k * direction[1]

                if row < 0 or row > N - 1 or col < 0 or col > M - 1:
                    break

                buffer += crossword[row][col]

                if not XMAS.startswith(buffer):
                    break

            else:
                count += 1


print(count)
