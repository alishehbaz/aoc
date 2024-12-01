# Ref: https://adventofcode.com/2024/day/1

def p2():

    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    arr1, arr2 = [], []

    for line in lines:
        a, b = line.split('   ')
        arr1.append(int(a))
        arr2.append(int(b))

    simScore = 0
    for i in arr1:
        count = 0
        for j in arr2:
            if i == j:
                count += 1
        simScore += i*count

    return simScore


ans = p2()
print(f'Similarity score is {ans}')
