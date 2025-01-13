from collections import Counter

# Ref: https://adventofcode.com/2018/day/2


def p1():
    threeCount = 0
    twoCount = 0

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    for line in lines:
        twoCount += matchFreq(Counter(line), 2)
        threeCount += matchFreq(Counter(line), 3)

    return twoCount * threeCount


def matchFreq(freqMap, valueToCheck):
    for val in freqMap.values():
        if val == valueToCheck:
            return 1

    return 0


ans = p1()
print(f"checksum = {ans}")
