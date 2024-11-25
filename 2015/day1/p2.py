def part2():

    currentFloor = 0
    with open("input.txt", "r") as file:
        for position, direction in enumerate(file.read()):
            if currentFloor < 0:
                return position
            if direction == '(':
                currentFloor += 1
            else:
                currentFloor -= 1

    return currentFloor


ans = part2()
print(f'Santa entered floor basement at {ans} position')
