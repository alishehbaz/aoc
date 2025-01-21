# Ref: https://adventofcode.com/2020/day/2


def p2():
        
    return sum([(policy.split()[2][int(policy.split()[0].split("-")[0])-1]==policy.split()[1][0]) ^ (policy.split()[2][int(policy.split()[0].split("-")[1])-1]==policy.split()[1][0]) for policy in [line.strip() for line in open("./input.txt")]])
    
ans = p2()
print(f"valid passwords based on 2nd policy = {ans}")
