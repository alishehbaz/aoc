def p1():

    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    # print(len(lines))
    for line in lines:
        # print(line)
        pass

    firstPart = lines[0]
    stack = []

    delimeter = 'mul'
    for i in range(len(firstPart)):
        threeLetterWindow = firstPart[i:i+3]
        # print(threeLetterWindow)
        if threeLetterWindow == delimeter:
            # print(threeLetterWindow)
            if firstPart[i+3] == '(':
                print('haha')
                i = i+3
                begin = i
                while i < len(firstPart):
                    if firstPart[i] == ']':
                        print(firstPart[i])
                        break
                    if firstPart[i] == ')':
                        print(firstPart[i])
                        end = i
                        break
                    i += 1
                print(firstPart[begin:end+1])
                stack.append(firstPart[begin+1:end+1-1])
                # print(stack)

                stack = [val for val in stack if val]
                processStack(stack)
                # print(stack)
                # if firstPart[i+4] == '(':
                #     print('ahah')
                # print(firstPart.split('mul'))


def processStack(stack):

    print(stack)
    res = 0
    for values in stack:
        a, b = values.split(',')
        print(a, b)
        res += int(a)*int(b)

    print(res)


p1()
