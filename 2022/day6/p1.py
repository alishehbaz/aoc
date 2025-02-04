def p1():

    lines = [line.strip() for line in open("./input.txt")]
    print(lines)

    print(getStartingMarker(lines, 4))


def getStartingMarker(signal, uniqueCharMarker):
    unique = set()
    for i in range(len(signal)-uniqueCharMarker-1):
        for j in range(uniqueCharMarker):
            unique.add(signal[i+j])
        if len(unique) == uniqueCharMarker:
            return i+uniqueCharMarker

        unique = set()


ans = p1()
print(f'ans = {ans}')
