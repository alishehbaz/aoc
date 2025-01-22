def p2():
    
    with open("./input.txt") as f:
        for line in f:
            captcha = line.strip()

    return getSum(captcha)


def getSum(captcha):
    
    _sum = 0

    for i in range(len(captcha)//2):
        if captcha[i] == captcha[i+(len(captcha)//2)]:
            _sum += int(captcha[i])*2
            
    return _sum


ans = p2()
print(f"solution to the captcha = {ans}")