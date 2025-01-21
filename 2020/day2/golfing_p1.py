# Ref: https://adventofcode.com/2020/day/2


def p1():
    
    return sum([int(policy.split()[0].split("-")[0]) <= policy.split()[2].count(policy.split()[1][0]) <= int(policy.split()[0].split("-")[1])
for policy in [line.strip() for line in open("./input.txt")]])

ans = p1()
print(f"valid passwords = {ans}")
