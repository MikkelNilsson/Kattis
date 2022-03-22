def vec(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def rotateclockwise(p):
    return (p[1], -p[0])

def dotp(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def turnRight(p1, p2, p3):
    return dotp(rotateclockwise(vec(p1, p2)), vec(p2, p3)) > 0

def turnLeft(p1, p2, p3):
    return dotp(rotateclockwise(vec(p1, p2)), vec(p2, p3)) < 0




inp = int(input())
while inp != 0:
    l = []
    for _ in inp:
        l.add(tuple(map(int, input().split())))

    l.sort()



    inp = int(input())