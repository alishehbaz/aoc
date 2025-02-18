def p1():

    instructions = [ins.rstrip().split('->') for ins in open("./input.txt")]

    variableMap = {}

    for i in range(len(instructions)):
        for j in range(len(instructions[i])):
            instructions[i][j] = instructions[i][j].strip()

    print(instructions)

    for instruction in instructions:

        numOrOp = instruction[0].split(" ")
        if (len(numOrOp) == 1):
            print(numOrOp)
            variableMap[instruction[1]] = int(numOrOp[0])
            print(variableMap)

        if len(numOrOp) == 2:
            if numOrOp[0] == 'NOT':
                source = numOrOp[1]
                print(instruction)
                dst = instruction[1]
                print(f'dst : {dst}')
                variableMap[dst] = ~variableMap[source]
                print(variableMap)


p1()
