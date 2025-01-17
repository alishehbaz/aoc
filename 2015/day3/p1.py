def part1():

    stack = []
    maxStackLength = -1

    with open('input.txt', "r") as file:
        lines = file.readlines()
        # stack.append(lines[0][0])
        for eachLine in lines:
            print(eachLine)
            for i in range(len(eachLine)):
                direction = eachLine[i]
                # print(f'index = {i}, directon = {direction}')
                if direction == '>' and stack and stack[-1] == '<':
                    stack.pop()
                    continue

                if direction == '<' and stack and stack[-1] == '>':
                    stack.pop()
                    continue

                if direction == '^' and stack and stack[-1] == 'v':
                    stack.pop()
                    continue

                if direction == 'v' and stack and stack[-1] == '^':
                    stack.pop()
                    continue

                stack.append(direction)
                maxStackLength = max(maxStackLength, len(stack))
                print(f'maxStacklength is {maxStackLength}')


part1()
