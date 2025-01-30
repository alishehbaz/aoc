# Ref: https://adventofcode.com/2022/day/4

def p2():

    shifts = [line.replace('\n', '') for line in open("input.txt")]

    notOverlapping = 0
    for i in range(len(shifts)):
        s1, s2 = shifts[i].split(',')
        startShift1, endShift1 = int(s1.split('-')[0]), int(s1.split('-')[1])
        startShift2, endShift2 = int(s2.split('-')[0]), int(s2.split('-')[1])

        if startShift2 > endShift1 or startShift1 > endShift2:
            notOverlapping += 1

    return len(shifts) - notOverlapping


ans = p2()
print(f'non-overlapping shifts = {ans}')
