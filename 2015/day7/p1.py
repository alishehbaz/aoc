from collections import defaultdict
# INCOMPLETE


def p1():

    instructions = [ins.rstrip().split('->') for ins in open("./input.txt")]

    variableMap = defaultdict(int)

    for i in range(len(instructions)):
        for j in range(len(instructions[i])):
            instructions[i][j] = instructions[i][j].strip()

    # print(instructions)

    for ip, instruction in enumerate(instructions):
        print(f'instruction pointer: {ip}')
        print(f'instruction: {instruction}')

        dst = instruction[-1]

        numOrOp = instruction[0].split(" ")
        if (len(numOrOp) == 1):
            if numOrOp[0].isdigit():
                variableMap[dst] = int(numOrOp[0])
            else:
                variableMap[dst] = variableMap[numOrOp[0]]

        if len(numOrOp) == 2:
            if numOrOp[0] == 'NOT':
                source = numOrOp[1]
                print(instruction)
                variableMap[dst] = ~variableMap[source] & 0xFFFF

        if len(numOrOp) > 2:
            print(numOrOp)
            if numOrOp[1] == 'AND':
                variableMap[dst] = variableMap[numOrOp[0]
                                               ] & variableMap[numOrOp[2]]

            if numOrOp[1] == 'OR':
                variableMap[dst] = variableMap[numOrOp[0]
                                               ] | variableMap[numOrOp[2]]

            if numOrOp[1] == 'LSHIFT':
                variableMap[dst] = variableMap[numOrOp[0]
                                               ] << int(numOrOp[2])

            if numOrOp[1] == 'RSHIFT':
                variableMap[dst] = variableMap[numOrOp[0]
                                               ] >> int(numOrOp[2])

    print(variableMap)

    print(f"value in {variableMap['a']}")


p1()
