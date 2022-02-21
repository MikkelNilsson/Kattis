input()

c = 0

for i in map(int, input().split()):
    if i < 0:
        c += 1

print(c)