from p1 import p1

testCases = [
    [2, 0, 0, 0, 99],
    [2, 3, 0, 6, 99],
    [2, 4, 4, 5, 99, 9801],
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
]

with open("testInput.txt") as f:
    for i, line in enumerate(f.readlines(), start=1):
        print(f'test: {i}')
        instructionSet = line.strip().split(',')
        print(f"expected : {testCases[i]}")
        print(f"actual: {p1(instructionSet)}")
