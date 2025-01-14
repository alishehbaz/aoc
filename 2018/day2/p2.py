# Ref: https://adventofcode.com/2018/day/2


def p2():

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            numOfDiffChars = getDiffScore(lines[i], lines[j])
            if numOfDiffChars == 1:
                return lines[i] and lines[j]


def getDiffScore(s, t):
    numOfDifferentChars = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            numOfDifferentChars += 1

    return numOfDifferentChars


ans = p2()
print(f"common between the two correct box IDs = {ans}")
