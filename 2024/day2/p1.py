# Ref: https://adventofcode.com/2024/day/2
def p1():

    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    safeCount = 0

    for line in lines:
        line = line.split(' ')

        for i in range(len(line)):
            line[i] = int(line[i])

        if isIncreasingOrDecreasing(line) and checkForDifference(line):
            safeCount += 1

    return safeCount

# The levels are either all increasing or all decreasing.


def isIncreasingOrDecreasing(arr):

    if arr[0] == arr[1]:
        return False

    isIncreasing = arr[0] < arr[1]

    for i in range(1, len(arr)-1):
        if isIncreasing:
            if arr[i] >= arr[i+1]:
                return False
        else:
            if arr[i] <= arr[i+1]:
                return False

    return True


# Any two adjacent levels differ by at least one and at most three.
def checkForDifference(arr):

    for i in range(len(arr)-1):

        diff = abs(arr[i]-arr[i+1])

        if diff >= 4:
            return False

    return True


ans = p1()
print(f'Safe Count: {ans}')
