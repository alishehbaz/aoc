def p1():
    
    with open("./input.txt") as f:
        for line in f:
            captcha = line.strip()

    return getSum(captcha)


def getSum(captcha):
    
    _sum = 0

    for i in range(1, len(captcha)):
        if captcha[i - 1] == captcha[i]:
            _sum += int(captcha[i])

    # circular check
    if captcha[len(captcha) - 1] == captcha[0]:
        _sum += int(captcha[0])

    return _sum


ans = p1()
print(f"solution to the captcha = {ans}")
