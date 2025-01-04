# Ref: https://adventofcode.com/2018/day/1

def p1():
    res = 0
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            res += int(line)
            
    print(res)


p1()