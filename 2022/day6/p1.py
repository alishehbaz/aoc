from solution import getStartingMarker


def p1():

    lines = open("./input.txt").readline()

    return getStartingMarker(lines, 4)


ans = p1()
print(f'{ans} characters need to be processed before the first start-of-packet marker is detected ')
