def p1():

    lines = open("./input.txt").readline()

    return getStartingMarker(lines, 4)


def getStartingMarker(signal, uniqueCharMarker):
    unique = set()
    for i in range(len(signal)-uniqueCharMarker-1):
        for j in range(uniqueCharMarker):
            unique.add(signal[i+j])
        if len(unique) == uniqueCharMarker:
            return i+uniqueCharMarker

        unique = set()


ans = p1()
print(f'{ans} characters need to be processed before the first start-of-packet marker is detected ')
