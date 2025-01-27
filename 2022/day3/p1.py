# Ref: https://adventofcode.com/2022/day/3


def p1():
    
    with open("input.txt") as f:
        rucksackData = [line.strip() for line in f]

    eachRucksackData = 0

    alphabets = {chr(i + 97): i + 1 for i in range(26)}

    for entry in rucksackData:
        p1, p2 = entry[: len(entry) // 2], entry[len(entry) // 2 :]
        commonLetter = "".join(set(p1).intersection(p2))
        if commonLetter.islower():
            score = alphabets[commonLetter]
        else:
            commonLetter = commonLetter.lower()
            score = alphabets[commonLetter] + 26
        eachRucksackData += score

    return eachRucksackData


ans = p1()
print(f"sum of the priorities of those item types = {ans}")
