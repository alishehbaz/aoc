# Ref: https://adventofcode.com/2015/day/2

def part1():

    totalWrappingPaper = 0
    smallestSide = float('inf')

    with open("input.txt", "r") as file:
        boxDimensions = file.readlines()
        for eachBoxDimension in boxDimensions:
            l, w, h = eachBoxDimension.strip('\n').split('x')
            l, w, h = int(l), int(w), int(h)
            smallestSide = min(l*w, w*h, h*l)
            totalWrappingPaper += 2 * (l*w + w*h + h*l) + smallestSide

    return totalWrappingPaper


ans = part1()
print(f'total wrapping paper needed in sq ft: {ans}')
