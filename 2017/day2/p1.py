def p1():
    
    checksum = 0
    
    with open("./input.txt") as f:
        rows =  f.readlines()
    
    for row in rows:
        row = [int(x) for x in row.strip().split()]     
        checksum += abs(int(max(row))-int(min(row)))
        
    return checksum
        
ans = p1()
print(f"checksum of spreadsheets = {ans}")
