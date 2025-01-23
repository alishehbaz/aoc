def p2():
    
    checksum = 0
    
    nums = []
    
    with open("./input.txt") as f:
        for row in f:
            nums.append(row.replace('\t', ' ').replace('\n', '').split())
        
    for numList in nums:
        for i in range(len(numList)):
            for j in range(i+1, len(numList)):
                if int(numList[i])%int(numList[j])==0:
                    checksum += int(numList[i])//int(numList[j])
                    break
                if int(numList[j])%int(numList[i])==0:
                    checksum += int(numList[j])//int(numList[i])
                    break
            
    return checksum
        
ans = p2()
print(f"checksum of spreadsheets = {ans}")
