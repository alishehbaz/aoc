# Ref: https://adventofcode.com/2020/day/1


def p1():
    
    with open("input.txt") as f:
        nums = [int(n) for n in [line.strip() for line in f]]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]


ans = p1()
print(f"two entries that sum to 2020 = {ans}")
