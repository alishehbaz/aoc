# Ref: https://adventofcode.com/2018/day/1

def p2():
    res = 0
    with open('input.txt') as f:
        lines = [int(line.strip()) for line in f]

    duplicateNotFound = True
    currFreq = 0
    hashset = set()
    hashset.add(currFreq)

    while duplicateNotFound:
        for i in range(len(lines)):
            currFreq += lines[i]
            if currFreq not in hashset:
                hashset.add(currFreq)
            else:
                duplicateNotFound = False
                break

    return res


ans = p2()
print(f'first frequency that is reached twice is {ans}')
