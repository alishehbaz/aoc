# Ref: https://adventofcode.com/2015/day/4
from solution import getLowestNumber


def p1():

    return getLowestNumber("ckczppom", 0, 1000000, 5)


ans = p1()
print(
    f"lowest number (when appended to the puzzle string) to produce a hash starting with five zeroes = {ans}"
)
