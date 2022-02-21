v = [int(i) for i in input().split()]
l = [int(input()) for _ in range(v[1])]

mn = mx = sum(l)

for _ in range(v[0]-v[1]):
    mn += -3
    mx += 3

print(str(mn/v[0]) + " " + str(mx/v[0]))