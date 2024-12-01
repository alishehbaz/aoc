# Ref: https://adventofcode.com/2024/day/1

def p1():

    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    arr1, arr2 = [], []

    for line in lines:
        a, b = line.split('   ')
        arr1.append(int(a))
        arr2.append(int(b))

    arr1.sort()
    arr2.sort()

    diffScore = 0

    for i in range(len(arr1)):
        diffScore += abs(arr2[i]-arr1[i])

    return diffScore


ans = p1()
print(f'Diff score is {ans}')
