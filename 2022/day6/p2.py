from solution import getStartingMarker


def p2():

    lines = open("./input.txt").readline()

    return getStartingMarker(lines, 14)


ans = p2()
print(f'{ans} characters need to be processed before the first start-of-packet marker is detected ')
