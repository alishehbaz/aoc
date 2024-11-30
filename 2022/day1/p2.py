from collections import defaultdict

# Ref: https://adventofcode.com/2022/day/1


def p2():

    k = 3
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    calorieMap = defaultdict(int)
    elf = 1
    for eachEntry in lines:
        if eachEntry == '':
            elf += 1
            continue
        calorieMap[elf] += int(eachEntry)

    s = 0
    while k:
        keyToDelete = max(calorieMap, key=calorieMap.get)
        s += calorieMap[keyToDelete]
        del calorieMap[keyToDelete]
        k -= 1

    return s


ans = p2()
print(f'Sum of top 3 highest calories is: {ans}')
