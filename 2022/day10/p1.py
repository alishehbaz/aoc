def p1():

    lines = [line.strip() for line in open('./input.txt')]

    cycles = [20, 60, 100, 140, 180, 220]

    return getSixSignalStrength(cycles, lines)


def getSignalStrength(cycle, signals):

    x = 1
    currentCycle = 0
    addCounter = 0
    signalStrength = 0
    for signal in signals:

        # if it is an add instruction
        if signal[0] == "a":

            ins, v = signal.split(" ")

            # since add takes to cycles
            currentCycle += 2

            # local counter only for add
            addCounter += 2

            # if we have reached the required cycle or have exceeded it
            if currentCycle >= cycle:
                signalStrength = cycle * x
                break

            # since we can only add when two cycles are complete
            if addCounter % 2 == 0:
                x += int(v)

        # if it is a noop instruction
        else:
            currentCycle += 1

    return signalStrength


def getSixSignalStrength(cycles, signals):

    signalSum = 0

    for cycle in cycles:

        signalSum += getSignalStrength(cycle, signals)

    return signalSum


ans = p1()
print(f"sum of these six signal strengths = {ans}")
