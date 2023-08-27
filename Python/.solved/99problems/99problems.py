v = int(input())

s = 99
d = abs(v - s)

while abs(v - (s + 100)) <= d:
    s += 100
    d = abs(v - s)

print(s)
