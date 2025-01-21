# Ref: https://adventofcode.com/2020/day/1


def p2():
    
    with open("input.txt") as f:
        nums = [int(n) for n in [line.strip() for line in f]]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    return nums[i] * nums[j] * nums[k]


ans = p2()
print(f"three entries that sum to 2020 = {ans}")
