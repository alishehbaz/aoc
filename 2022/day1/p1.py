from collections import defaultdict

# Ref: https://adventofcode.com/2022/day/1


def p1():

    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    calorieMap = defaultdict(int)
    elf = 1
    for eachEntry in lines:
        if eachEntry == '':
            elf += 1
            continue
        calorieMap[elf] += int(eachEntry)

    return max(calorieMap.values())


ans = p1()
print(f'The highest number of calories carried by Elf : {ans}')
