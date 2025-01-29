# Ref: https://adventofcode.com/2022/day/4

def p1():

    shifts = [line.replace('\n', '') for line in open("input.txt")]

    count = 0

    for i in range(len(shifts)):
        s1, s2 = shifts[i].split(',')
        startShift1, endShift1 = int(s1.split('-')[0]), int(s1.split('-')[1])
        startShift2, endShift2 = int(s2.split('-')[0]), int(s2.split('-')[1])

        # s1 contains s2
        if startShift2 >= startShift1 and endShift2 <= endShift1:
            count += 1

        # s2 contains s1
        elif startShift1 >= startShift2 and endShift1 <= endShift2:
            count += 1

        # no overlap
        else:
            print(i+1, "NO OVERLAP", (startShift1, endShift1),
                  (startShift2, endShift2))

    return count


ans = p1()
print(f'overlapping shifts = {ans}')
