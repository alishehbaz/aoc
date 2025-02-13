# Ref: https://adventofcode.com/2015/day/4
from solution import getLowestNumber


def p2():

    return getLowestNumber("ckczppom", 0, 10000000, 6)


ans = p2()
print(
    f"lowest number (when appended to the puzzle string) to produce a hash starting with six zeroes = {ans}"
)
