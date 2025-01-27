# Ref: https://adventofcode.com/2022/day/3


def p2():

    with open("input.txt") as f:
        rucksackData = [line.strip() for line in f]

    eachRucksackData = 0

    alphabets = {chr(i+97): i+1 for i in range(26)}

    for _, j in enumerate(range(0, len(rucksackData)-2, 3)):
        e1, e2, e3 = set(rucksackData[j]), set(
            rucksackData[j+1]), set(rucksackData[j+2])
        commonLetter = ''.join(set.intersection(e1, e2, e3))
        if commonLetter.islower():
            score = alphabets[commonLetter]
        else:
            commonLetter = commonLetter.lower()
            score = alphabets[commonLetter] + 26
        eachRucksackData += score

    return eachRucksackData


ans = p2()
print(f"sum of the priorities of those item types = {ans}")
