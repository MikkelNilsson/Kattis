b = int(input())

u = 0
l = 1
height = 0
while (u < b):
    l += 2
    u += l*l
    height += 1

print(height)