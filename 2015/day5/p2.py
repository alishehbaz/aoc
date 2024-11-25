# Ref: https://adventofcode.com/2015/day/5

def part2():

    niceStrings = 0

    with open("input.txt", "r") as file:
        lines = file.readlines()
        for eachStr in lines:
            eachStr = eachStr.strip('\n')
            if hasNonOverlappingPairs(eachStr) and hasALen3Palindrome(eachStr):
                niceStrings += 1

    return niceStrings


# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
def hasNonOverlappingPairs(s):

    for i in range(len(s)-1):
        for j in range(i+2, len(s)-1):
            if s[i:i+2] == s[j:j+2]:
                return True

    return False


# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi(efe), or even aaa. Basically a palindrome of length 3
def hasALen3Palindrome(s):

    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True

    return False


ans = part2()
print(f'total nice strings based on the rules are: {ans}')
