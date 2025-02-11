# Ref: https://adventofcode.com/2015/day/4

import hashlib


def p1():
    puzzleInput = "ckczppom"

    for i in range(1000000):
        toBeHashed = puzzleInput + str(i)

        md5Hash = hashlib.md5(toBeHashed.encode("utf-8")).hexdigest()

        if md5Hash[:5] == "00000":
            return i


ans = p1()
print(
    f"lowest number (when appended to the puzzle string) to produce a hash starting with five zeroes = {ans}"
)
