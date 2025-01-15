import math


def p1():

    return sum([((math.floor(int(line.strip())/3))-2) for line in open("input.txt")])


ans = p1()
print(f'sum of the fuel requirements = {ans}')
