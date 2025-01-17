# INCOMPLETE

import re


def p1():

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open("input.txt") as f:
        lines = [line.strip() for line in f]
        matches = []
        for line in lines:
            matches += re.findall(pattern, line)

    res = 0
    for a, b in matches:
        res += int(a)*int(b)

    print(res)


p1()
