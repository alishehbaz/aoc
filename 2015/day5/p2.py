def part1():

    niceStrings = 0

    with open("input.txt", "r") as file:
        lines = file.readlines()
        for eachStr in lines:
            eachStr = eachStr.strip('\n')

            if hasAtleast3Vowels(eachStr) and hasCharTwiceInARow(eachStr) and hasForbiddenStrings(eachStr):
                niceStrings += 1

        print(niceStrings)


def hasAtleast3Vowels(s):

    vowels = 'aeiou'
    vowelsCount = 0

    for c in s:
        if c in vowels:
            vowelsCount += 1
        if vowelsCount == 3:
            return True

    return False


def hasCharTwiceInARow(s):

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def hasForbiddenStrings(s):

    forbiddenStrings = ['ab', 'cd', 'pq', 'xy']
    for i in range(len(s)-1):
        if s[i:i+2] in forbiddenStrings:
            return False

    return True


ans = part1()
print(f'total nice strings based on the rules are: {ans}')
