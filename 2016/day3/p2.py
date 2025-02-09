def p1():
    
    triangles = [triangle.strip() for triangle in open("./input.txt")]

    validTriangles = 0

    for i in range(0, len(triangles), 3):
        t1s1, t2s1, t3s1 = triangles[i].split()
        t1s2, t2s2, t3s2 = triangles[i+1].split()
        t1s3, t2s3, t3s3 = triangles[i+2].split()
        if isValidTriangle(t1s1, t1s2, t1s3):
            validTriangles += 1
            
        if isValidTriangle(t2s1, t2s2, t2s3):
            validTriangles += 1
            
        if isValidTriangle(t3s1, t3s2, t3s3):
            validTriangles += 1

    return validTriangles

def isValidTriangle(s1,s2,s3):
    
    return int(s1) + int(s2) > int(s3) and int(s1) + int(s3) > int(s2) and int(s3) + int(s2) > int(s1)

ans = p1()
print(f"valid triangles based on column reads = {ans}")
