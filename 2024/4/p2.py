#! /usr/bin/env python3


with open("input.txt", "r") as f:
    crossword = [[char for char in line.strip()] for line in f]

N = len(crossword)
M = len(crossword[0])

count = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):

        if crossword[i][j] == "A":
            buffer1 = crossword[i - 1][j - 1] + "A" + crossword[i + 1][j + 1]
            buffer2 = crossword[i - 1][j + 1] + "A" + crossword[i + 1][j - 1]

            if buffer1 == "MAS" or buffer1 == "SAM":
                if buffer2 == "MAS" or buffer2 == "SAM":
                    count += 1

print(count)
