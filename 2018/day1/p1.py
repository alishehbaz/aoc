# Ref: https://adventofcode.com/2018/day/1

def p1():
    res = 0
    with open('input.txt') as f:
        res = sum([int(n) for n in [line.strip() for line in f]])
    return res


ans = p1()
print(f'final frequency is {ans}')