n = int(input())
a, b = 1, 0
for _ in range(n):
    tempb = a + b
    a = b
    b = tempb

print(a, b)