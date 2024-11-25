# Ref: https://adventofcode.com/2015/day/1

def part1():

    currentFloor = 0
    with open("input.txt", "r") as file:
        for direction in file.read():
            if direction == '(':
                currentFloor += 1
            else:
                currentFloor -= 1

    return currentFloor


ans = part1()
print(f'Santa is currently at floor: {ans}')
