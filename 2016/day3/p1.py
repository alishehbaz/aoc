def p1():
    
    triangles = [triangle.strip() for triangle in open("./input.txt")]

    validTriangles = 0

    for triangle in triangles:
        s1, s2, s3 = triangle.split()
        if int(s1) + int(s2) > int(s3) and int(s1) + int(s3) > int(s2) and int(s3) + int(s2) > int(s1):
            validTriangles += 1

    return validTriangles


ans = p1()
print(f"valid triangles = {ans}")
