# Ref: https://adventofcode.com/2020/day/1


def p1():

    with open("input.txt") as f:
        nums = [line.strip() for line in f]

    
    for i in len(nums):
        for j in (i+1, len(nums)):
            print(nums[i], nums[j])
            if nums[i]+nums[j]==2020:
                return nums[i]*nums[j]
                



ans = p1()
print(f"checksum = {ans}")
