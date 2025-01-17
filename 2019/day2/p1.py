# INCOMPLETE
def p1(instructions):

    print(instructions)

    pc = 0
    #  instructions[pc] != 99
    while pc < len(instructions):
        # print(pc)
        opcode = instructions[pc]

        if opcode == 1:
            pc += 1  # read from reg
            regA = instructions[instructions[pc]]
            print(f'read {regA} from {pc}')

            pc += 1  # read from reg
            regB = instructions[instructions[pc]]
            print(f'read {regB} from {pc}')

            pc += 1  # write to this reg
            regC = instructions[pc]
            res = regA+regB
            print(f'add: writing {res} to {pc}')

            # write
            instructions[instructions[pc]] = regA+regB

        if opcode == 2:
            pc += 1  # read from reg
            regA = instructions[instructions[pc]]
            print(f'read {regA} from {pc}')

            pc += 1  # read from reg
            regB = instructions[instructions[pc]]
            print(f'read {regB} from {pc}')

            pc += 1  # write to this reg
            # regC = instructions[pc]
            res = regA*regB
            print(f'multiple: writing {res} to {pc}')

            # write
            instructions[instructions[pc]] = regA*regB

        if opcode == 99:
            break

        pc += 1

    print(instructions)
    return instructions


if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = [int(line) for line in f.read().rstrip().split(',')]
    ans = p1(instructions)
# print(f'ans = {ans}')
