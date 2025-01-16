# Ref: https://adventofcode.com/2019/day/1
import math


def p2():

    _sum = 0
    lines = [int(line.strip()) for line in open("input.txt")]

    for num in lines:
        while num > 0:
            num = math.floor(num/3)-2
            if num > 0:
                _sum += num

    return _sum


ans = p2()
print(f'sum of the fuel requirements = {ans}')
