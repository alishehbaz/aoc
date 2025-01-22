def p1():
    
    captcha = open("./input.txt").readline()
    
    return sum([int(captcha[i])*2 for i in range(len(captcha)//2) if captcha[i] == captcha[i+(len(captcha)//2)]])
            
ans = p1()
print(f"solution to the captcha = {ans}")
