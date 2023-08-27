c, l = float(input()), int(input())
sum = 0.0
for _ in range(l):
    w, l = map(float, input().split())
    sum += w * l * c

print("{:.7f}".format(sum))