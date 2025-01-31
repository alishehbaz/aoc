# Ref: https://adventofcode.com/2022/day/5

from parse import parseInput


def p1():

    instructions = [line.strip() for line in open("./input.txt")]

    crateMoverType = 'CrateMover 9000'

    moveInstructions, stackPileMap = parseInput(instructions)

    print(moveInstructions, stackPileMap)


p1()
