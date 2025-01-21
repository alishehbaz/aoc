# Ref: https://adventofcode.com/2020/day/2


def p1():
    
    with open("./input.txt") as f:
        passwordPolicies = [line.strip() for line in f]

    validPasswords = 0

    for policy in passwordPolicies:
        rule, char, password = policy.split()

        if isValid(rule, char, password):
            validPasswords += 1

    return validPasswords


def isValid(rule, char, password):
    
    minFreq, maxFreq = rule.split("-")
    char = char[0]

    return int(minFreq) <= password.count(char) <= int(maxFreq)

ans = p1()
print(f"valid passwords = {ans}")
