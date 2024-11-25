# Ref: https://adventofcode.com/2015/day/2

def part2():

    totalRibbonPaper = 0

    with open("input.txt", "r") as file:
        boxDimensions = file.readlines()
        for eachBoxDimension in boxDimensions:
            l, w, h = eachBoxDimension.strip('\n').split('x')
            l, w, h = int(l), int(w), int(h)
            smallestSidePerimeter = 2 * \
                (smallestSides(l, w, h)[0] + smallestSides(l, w, h)[1])
            totalRibbonPaper += smallestSidePerimeter + l*w*h

    return totalRibbonPaper


def smallestSides(l, w, h):

    dimensions = [l, w, h]
    dimensions.sort()

    return dimensions[0], dimensions[1]


ans = part2()
print(f'total wrapping paper needed for the ribbon in sq ft: {ans}')
