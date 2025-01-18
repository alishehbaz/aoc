# Ref: https://adventofcode.com/2019/day/2
opcodeMappings = {
    "ADD": 1,
    "MULTIPLY": 2
}


def p1(instructions):

    pc = 0  # program counter

    while pc < len(instructions):
        opcode = instructions[pc]

        if opcode == 1:
            pc = performOp(instructions, opcodeMappings["ADD"], pc)
        if opcode == 2:
            pc = performOp(instructions, opcodeMappings["MULTIPLY"], pc)

        if opcode == 99:
            break

        pc += 1

    return instructions


def performOp(instructions, opcode, pc):

    pc += 1  # read from reg
    regA = instructions[instructions[pc]]
    print(f'reading val: {regA} from memory loc: {instructions[pc]}')

    pc += 1  # read from reg
    regB = instructions[instructions[pc]]
    print(f'reading val: {regB} from memory loc: {instructions[pc]}')

    if opcode == 1:
        res = regA+regB

    if opcode == 2:
        res = regA*regB

    pc += 1

    print(
        f'writing val: {res} to memory loc: {instructions[instructions[pc]]}')
    # write to this reg
    instructions[instructions[pc]] = res

    return pc


if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = [int(line) for line in f.read().rstrip().split(',')]
    ans = p1(instructions)
    print(f'ans = {ans[0]}')
