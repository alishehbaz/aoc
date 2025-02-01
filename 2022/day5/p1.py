# Ref: https://adventofcode.com/2022/day/5

from parse import parseInput


def p1():

    instructions = [line.strip() for line in open("./input.txt")]

    crateMoverType = 'CrateMover 9000'

    moveInstructions, stackPileMap = parseInput(instructions)

    # print(moveInstructions, stackPileMap)

    for instruction in moveInstructions:

        instruction = instruction.split(' ')
        boxesToMove, fromStack, toStack = int(instruction[1]), int(
            instruction[3]), int(instruction[5])

        boxesToMove = getBoxesToBeMoved(stackPileMap, fromStack, boxesToMove)
        addBoxesToStack(stackPileMap, toStack, boxesToMove, crateMoverType)

        return getTopElements(stackPileMap)


def getBoxesToBeMoved(stackPileMap, fromStack, k):
    popped = []
    while k:
        box = stackPileMap[fromStack].pop()
        popped.append(box)
        k -= 1

    return popped


def addBoxesToStack(stackPileMap, toStack, toAdd, crateMoverType):
    if crateMoverType == 'CrateMover 9000':
        stackPileMap[toStack].extend(toAdd)
    if crateMoverType == 'CrateMover 90001':
        stackPileMap[toStack].extend(toAdd[::-1])


def getTopElements(stackPileMap):

    topBoxesString = ''

    for value in stackPileMap.values():
        topBoxesString += value[-1]

    return topBoxesString


ans = p1()
print(f'ans = {ans}')
