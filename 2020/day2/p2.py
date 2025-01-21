# Ref: https://adventofcode.com/2020/day/2


def p2():
    
    with open("./input.txt") as f:
        passwordPolicies = [line.strip() for line in f]

    validPasswords = 0

    for policy in passwordPolicies:
        rule, char, password = policy.split()

        if isValid(rule, char, password):
            validPasswords += 1

    return validPasswords


def isValid(rule, char, password):
    
    pos1, pos2 = rule.split("-")
    
    pos1, pos2 = int(pos1), int(pos2)
    
    # rules are based on the assumption that the strings are not zero indexeded
    pos1 -=1
    pos2 -=1
    
    char = char[0]
    
    return (password[pos1]==char) ^ (password[pos2]==char)
    
ans = p2()
print(f"valid passwords based on 2nd policy = {ans}")
